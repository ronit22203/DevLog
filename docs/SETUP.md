# 🔧 Detailed Setup Instructions

## Prerequisites

### System Requirements
- **Python 3.8 or higher** - Check with `python3 --version`
- **pip package manager** - Usually comes with Python
- **Terminal/Command Line access**

### Google API Key Setup

1. **Go to Google AI Studio**
   - Visit: https://makersuite.google.com/app/apikey
   - Sign in with your Google account

2. **Create API Key**
   - Click "Create API Key"
   - Select existing project or create new one
   - Copy the generated API key

3. **Set Environment Variable**
   
   **For macOS/Linux (Bash/Zsh):**
   ```bash
   export GOOGLE_API_KEY="your-api-key-here"
   
   # Add to shell profile to persist across sessions
   echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.zshrc
   # or for bash users:
   echo 'export GOOGLE_API_KEY="your-api-key-here"' >> ~/.bashrc
   
   # Reload your shell
   source ~/.zshrc  # or ~/.bashrc
   ```
   
   **For Windows (PowerShell):**
   ```powershell
   $env:GOOGLE_API_KEY="your-api-key-here"
   
   # To persist across sessions:
   [Environment]::SetEnvironmentVariable("GOOGLE_API_KEY", "your-api-key-here", "User")
   ```

## Installation Methods

### Method 1: Quick Setup (Recommended)

```bash
# Clone the repository
git clone https://github.com/yourusername/devlog.git
cd devlog

# Run setup (installs dependencies and checks configuration)
make setup

# Test the installation
make test
```

### Method 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/devlog.git
cd devlog

# Install Python dependencies
pip install -r requirements.txt

# Set your API key (see above)
export GOOGLE_API_KEY="your-api-key-here"

# Test the setup
python -c "import google.generativeai; print('✅ Dependencies installed successfully')"
```

### Method 3: Virtual Environment (Recommended for Development)

```bash
# Clone the repository
git clone https://github.com/yourusername/devlog.git
cd devlog

# Create virtual environment
python3 -m venv devlog-env

# Activate virtual environment
source devlog-env/bin/activate  # On Windows: devlog-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set API key and test
export GOOGLE_API_KEY="your-api-key-here"
make test
```

## Configuration Options

### Environment Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `GOOGLE_API_KEY` | **Required** Google Gemini API key | None | `"AIza...xyz"` |
| `DEVLOG_FILE` | Path to your log file | `devlog.md` | `"/path/to/my-log.md"` |
| `DEVLOG_MODEL` | Gemini model to use | `gemini-1.5-flash` | `"gemini-1.5-pro"` |

### Available Models

- **gemini-1.5-flash** (default) - Fast and efficient, good for daily use
- **gemini-1.5-pro** - More powerful for complex analysis and insights

### Custom Log File Location

```bash
# Use a different log file
export DEVLOG_FILE="/path/to/my-project/project-log.md"
make log

# Or specify per command
DEVLOG_FILE="./team-log.md" make log
```

## Troubleshooting

### Common Issues

**1. "google-generativeai package not found"**
```bash
# Solution: Install dependencies
make install
# or
pip install google-generativeai
```

**2. "GOOGLE_API_KEY environment variable not found"**
```bash
# Solution: Set your API key
export GOOGLE_API_KEY="your-api-key-here"

# Check if it's set
echo $GOOGLE_API_KEY
```

**3. "API quota exceeded"**
- You've hit the free tier limit (50 requests/day)
- Wait 24 hours for reset, or upgrade to paid plan
- See: https://ai.google.dev/gemini-api/docs/rate-limits

**4. "Permission denied" when running make commands**
```bash
# Solution: Make scripts executable
chmod +x src/*.py
```

**5. Import errors in Python scripts**
```bash
# Solution: Run from project root directory
cd /path/to/devlog
make log  # Instead of: python src/logger.py
```

### Getting Help

1. **Check the logs**: Look for error messages in the terminal output
2. **Verify setup**: Run `make test` to check your configuration
3. **Try the demo**: Run `make demo` to test with sample data
4. **Check API key**: Ensure your Google API key is valid and has quota remaining

### Advanced Configuration

**Using a different Python interpreter:**
```bash
# Specify Python version in Makefile
python3.9 src/logger.py
```

**Multiple log files for different projects:**
```bash
# Create project-specific aliases
alias worklog="DEVLOG_FILE='work-log.md' make log"
alias personallog="DEVLOG_FILE='personal-log.md' make log"
```

**Running in Docker:**
```bash
# Create a simple Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV GOOGLE_API_KEY=""
CMD ["python", "src/logger.py"]
```

## Upgrading

```bash
# Pull latest changes
git pull origin main

# Update dependencies
make install

# Test the update
make test
```

## Development Setup

If you want to contribute to DevLog:

```bash
# Install development dependencies
make dev-install

# Format code
make format

# Lint code
make lint

# Run tests (when implemented)
pytest
```
