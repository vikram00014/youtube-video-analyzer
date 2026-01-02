from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
import re
import json
import os

app = Flask(__name__)

# Initialize Gemini client - Use environment variable for security
GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', 'AIzaSyDWJW68z4wgOy8gb0gmSbDkKlDaYDCfZ5g')
client = genai.Client(api_key=GEMINI_API_KEY)

def extract_video_id(url):
    """Extract YouTube video ID from various URL formats"""
    # Remove extra parameters first
    url = url.split('&')[0]  # Remove &list=, &index=, etc.
    
    patterns = [
        r'(?:v=|/)([0-9A-Za-z_-]{11}).*',
        r'(?:embed/)([0-9A-Za-z_-]{11})',
        r'(?:youtu\.be/)([0-9A-Za-z_-]{11})',
        r'(?:watch\?v=)([0-9A-Za-z_-]{11})',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            video_id = match.group(1)
            # Clean up any remaining query parameters
            video_id = video_id.split('?')[0].split('&')[0]
            return video_id
    return None

def get_transcript(video_id):
    """Get transcript from YouTube video"""
    try:
        ytt_api = YouTubeTranscriptApi()
        # Try to get transcript in any available language
        transcript_list = ytt_api.list(video_id)
        
        # Get the first available transcript (prefer English if available)
        available_transcripts = list(transcript_list)
        if not available_transcripts:
            return None, "No transcripts available for this video"
        
        # Try English first, then any other language
        transcript = None
        for t in available_transcripts:
            if t.language_code.startswith('en'):
                transcript = t
                break
        
        if transcript is None:
            transcript = available_transcripts[0]  # Use first available
        
        # Fetch the transcript
        fetched = transcript.fetch()
        full_transcript = " ".join([item.text for item in fetched])
        
        print(f"[DEBUG] Got transcript in language: {transcript.language_code}")
        return full_transcript, None
    except Exception as e:
        return None, str(e)

def analyze_with_gemini(transcript, video_title=""):
    """Use Gemini to analyze transcript and generate notes"""
    prompt = f"""You are an expert note-taker and educator. Analyze the following YouTube video transcript and create comprehensive, well-structured notes.

Video Title: {video_title}

Transcript:
{transcript}

Please provide:
1. **📌 Summary** - A brief 2-3 sentence overview of the video content
2. **🎯 Key Points** - Main takeaways in bullet points
3. **📝 Detailed Notes** - Organized notes with headings and subheadings
4. **💡 Key Concepts** - Important terms or concepts explained
5. **✅ Action Items** - Any actionable advice or steps mentioned
6. **🔗 Related Topics** - Suggested topics for further learning

Format the response in clean Markdown for easy reading."""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text, None
    except Exception as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    url = data.get('url', '')
    
    print(f"[DEBUG] Received URL: {url}")
    
    if not url:
        return jsonify({'error': 'Please provide a YouTube URL'}), 400
    
    # Extract video ID
    video_id = extract_video_id(url)
    print(f"[DEBUG] Extracted video_id: {video_id}")
    
    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL'}), 400
    
    # Get transcript
    print(f"[DEBUG] Fetching transcript for: {video_id}")
    transcript, error = get_transcript(video_id)
    if error:
        print(f"[DEBUG] Transcript error: {error}")
        return jsonify({'error': f'Could not get transcript: {error}. Make sure the video has captions/subtitles available.'}), 400
    
    print(f"[DEBUG] Transcript length: {len(transcript)}")
    
    # Analyze with Gemini
    print(f"[DEBUG] Sending to Gemini for analysis...")
    notes, error = analyze_with_gemini(transcript)
    if error:
        print(f"[DEBUG] Gemini error: {error}")
        return jsonify({'error': f'Analysis failed: {error}'}), 500
    
    print(f"[DEBUG] Analysis complete!")
    return jsonify({
        'success': True,
        'video_id': video_id,
        'notes': notes,
        'transcript_length': len(transcript)
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
