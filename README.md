# 📺 YouTube Video Analyzer

AI-powered YouTube video analysis system that generates comprehensive notes from video transcripts using Gemini AI.

## 🌟 Features

- 📝 Extract transcripts from YouTube videos (any language)
- 🤖 AI-powered note generation with Gemini
- 🎯 Structured notes with summaries, key points, and action items
- 💾 Local history tracking
- 📋 Copy/download notes as Markdown
- 🌍 Multi-language transcript support (Hindi, English, Spanish, etc.)
- 📊 Beautiful dashboard UI

## 🚀 Live Demo

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR-USERNAME/ytdl)

[Live Site - Coming Soon]

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **AI:** Google Gemini 2.5 Flash API
- **Transcript:** youtube-transcript-api
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Deployment:** Vercel

## 📦 Local Installation

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/ytdl.git
cd ytdl

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set your API key
# Create .env file or set environment variable
set GEMINI_API_KEY=your_api_key_here  # Windows
# or
export GEMINI_API_KEY=your_api_key_here  # Linux/Mac

# Run locally
python app.py
```

Visit: `http://localhost:5000`

## 🔑 API Key Setup

Get your free Gemini API key from: [Google AI Studio](https://aistudio.google.com/apikey)

### For Local Development:
Set environment variable:
```bash
set GEMINI_API_KEY=your_api_key_here
```

### For Vercel Deployment:
1. Go to your Vercel project settings
2. Navigate to Environment Variables
3. Add: `GEMINI_API_KEY` = `your_api_key_here`

## 📝 Usage

1. Open the web app
2. Paste any YouTube video URL
3. Click "Generate Notes"
4. Get AI-generated comprehensive notes with:
   - 📌 Summary
   - 🎯 Key Points
   - 📝 Detailed Notes
   - 💡 Key Concepts
   - ✅ Action Items
   - 🔗 Related Topics
5. Copy to clipboard or download as Markdown

## 🌐 Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR-USERNAME/ytdl)

Or manually:

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy
vercel

# Add environment variable
vercel env add GEMINI_API_KEY
```

## 🔧 Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GEMINI_API_KEY` | Your Google Gemini API key | Yes |
| `PORT` | Server port (default: 5000) | No |

## 📂 Project Structure

```
ytdl/
├── app.py                 # Flask backend
├── templates/
│   └── index.html        # Frontend dashboard
├── requirements.txt      # Python dependencies
├── vercel.json          # Vercel configuration
├── Procfile             # Process file for deployment
├── runtime.txt          # Python version
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🎨 Features in Detail

### AI-Powered Analysis
- Uses Google Gemini 2.5 Flash for fast, accurate analysis
- Structured output with proper formatting
- Supports multiple languages

### Smart Transcript Fetching
- Automatically detects available languages
- Prefers English when available
- Falls back to any available language

### User-Friendly Interface
- Modern, responsive design
- YouTube-inspired theme
- Real-time loading states
- Toast notifications
- History tracking (localStorage)

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

MIT License - feel free to use for personal or commercial projects

## 🙏 Acknowledgments

- Google Gemini API
- YouTube Transcript API
- Flask Framework
- Vercel for hosting

---

Made with ❤️ for better learning from YouTube videos
