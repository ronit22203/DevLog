# DevLog - AI-Powered Daily Development Logger

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**DevLog** is a simple yet powerful CLI tool that helps developers track their daily progress, learnings, and challenges using AI-powered insights. Built for developers who want to reflect on their journey and get intelligent feedback on their growth.

[![Watch the video](https://cdn.loom.com/sessions/thumbnails/95a1a48b764f4450944ef5f57503b7d4-with-play.gif)](https://www.loom.com/share/95a1a48b764f4450944ef5f57503b7d4)

## Features

- **Simple CLI interface** - Quick daily logging with three focused questions
- **AI-powered insights** - Chat with your logs using Google Gemini API
- **Markdown format** - Human-readable logs with timestamps
- **Easy setup** - One-command installation and configuration
- **Intelligent search** - Ask questions about your development journey
- **Self-reflection** - Track mood, progress, and blockers over time

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Google API key (free from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/devlog.git
cd devlog
```

2. **Set up the environment**
```bash
make setup
```

3. **Configure your API key**
```bash
export GOOGLE_API_KEY="your-api-key-here"
# Add to your shell profile to persist:
echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.zshrc
```

4. **Start logging!**
```bash
make log    # Add a daily entry
make chat   # Chat with your logs
```

## Usage

### Daily Logging
```bash
make log
```
This will prompt you with three reflection questions:
1. **📚 What did you learn today?** - Capture new knowledge and insights
2. **🚀 What decision moved your project forward?** - Track important decisions
3. **What's unclear or bothering you?** - Document challenges and blockers

### AI Chat Interface
```bash
make chat
```
Ask questions like:
- "What did I learn this week about React?"
- "Show me my recent decisions about database design"
- "What challenges have I been facing lately?"
- "Summarize my progress on the authentication feature"

### Other Commands
```bash
make help     # Show all available commands
make test     # Test your setup
make clean    # Clean up temporary files
```

## 📁 Project Structure

```
devlog/
├── README.md                 # This file
├── Makefile                 # Easy-to-use commands
├── requirements.txt         # Python dependencies
├── src/
│   ├── logger.py           # Daily logging functionality
│   ├── assistant.py        # AI chat interface
│   └── config.py           # Configuration management
├── examples/
│   └── sample_log.md       # Example log file
└── docs/
    ├── SETUP.md            # Detailed setup instructions
    └── EXAMPLES.md         # Usage examples and tips
```

## Advanced Configuration

### Custom Log File Location
```bash
export DEVLOG_FILE="path/to/your/logfile.md"
```

### Different AI Models
Edit `src/config.py` to use different Gemini models:
- `gemini-1.5-flash` (default) - Fast and efficient
- `gemini-1.5-pro` - More powerful for complex queries

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Make your changes** and add tests
4. **Commit your changes** (`git commit -m 'Add amazing feature'`)
5. **Push to the branch** (`git push origin feature/amazing-feature`)
6. **Open a Pull Request**

### Development Setup
```bash
make dev-install  # Install development dependencies
make test         # Run tests
```

## Example Log Entry

```markdown
## 2025-07-30 - Daily Log (14:30)

### 📚 What I Learned Today
Learned about Docker multi-stage builds to optimize image size. Reduced our production image from 1.2GB to 300MB by separating build and runtime dependencies.

### 🚀 Decision That Moved My Project Forward
Decided to implement Redis caching for our API responses. This should reduce database load by ~70% based on our query patterns.

### What I'm Unclear About / What's Bothering Me
Still struggling with the websocket connection drops in production. Need to investigate if it's a load balancer issue or application-level problem.

---
```

## 🎯 Use Cases

- **Individual developers** tracking their learning journey
- **Team leads** understanding team challenges and progress
- **Students** reflecting on coding bootcamp or course progress
- **Open source contributors** documenting their contribution journey
- **Technical writers** gathering insights for blog posts or documentation

## 🔐 Privacy & Security

- All logs are stored locally on your machine
- API calls to Google Gemini only send your questions and relevant log context
- No personal data is stored or transmitted beyond what's necessary for AI responses
- You have full control over your data

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Google Gemini API](https://ai.google.dev/)
- Inspired by the daily standup format and reflection practices
- Thanks to the developer community for feedback and contributions

## 🐛 Issues & Support

- **Bug reports**: [GitHub Issues](https://github.com/yourusername/devlog/issues)
- **Feature requests**: [GitHub Discussions](https://github.com/yourusername/devlog/discussions)
- **Questions**: Check out our [docs/](docs/) folder

---

**Happy logging! Track your journey, reflect with AI, and grow as a developer.**
