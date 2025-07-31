# DevLog - AI-Powered Daily Development Logger
# Quick commands for tracking your development journey

.PHONY: help install setup log chat clean test
.DEFAULT_GOAL := help

# Colors for output
BLUE := \033[36m
GREEN := \033[32m
YELLOW := \033[33m
RED := \033[31m
RESET := \033[0m

help: ## Show this help message
	@echo "$(BLUE)🔥 DevLog - AI-Powered Daily Development Logger$(RESET)"
	@echo "$(BLUE)================================================$(RESET)"
	@echo ""
	@echo "$(GREEN)Available commands:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  $(YELLOW)%-12s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(BLUE)Quick Start:$(RESET)"
	@echo "  1. $(YELLOW)make setup$(RESET)    - Install dependencies and configure"
	@echo "  2. $(YELLOW)make log$(RESET)      - Add a daily log entry"
	@echo "  3. $(YELLOW)make chat$(RESET)     - Chat with your logs using AI"

install: ## Install Python dependencies
	@echo "$(BLUE)📦 Installing dependencies...$(RESET)"
	pip install -r requirements.txt
	@echo "$(GREEN)✅ Dependencies installed!$(RESET)"

setup: install ## Complete setup including API key configuration
	@echo "$(BLUE)🔧 Setting up DevLog...$(RESET)"
	@echo ""
	@if [ -z "$$GOOGLE_API_KEY" ]; then \
		echo "$(YELLOW)⚠️  GOOGLE_API_KEY not found in environment$(RESET)"; \
		echo "$(BLUE)💡 Get your API key from: https://makersuite.google.com/app/apikey$(RESET)"; \
		echo "$(BLUE)💡 Then run: export GOOGLE_API_KEY='your-api-key-here'$(RESET)"; \
		echo "$(BLUE)💡 Add it to your shell profile (.bashrc/.zshrc) to persist$(RESET)"; \
	else \
		echo "$(GREEN)✅ GOOGLE_API_KEY found!$(RESET)"; \
	fi
	@echo ""
	@echo "$(GREEN)🚀 Setup complete! Try 'make log' to start logging$(RESET)"

log: ## Add a new daily log entry
	@echo "$(BLUE)📝 Starting daily log entry...$(RESET)"
	python src/logger.py

chat: ## Start AI chat with your logs  
	@echo "$(BLUE)🔥 Starting AI assistant...$(RESET)"
	@if [ -z "$$GOOGLE_API_KEY" ]; then \
		echo "$(RED)❌ GOOGLE_API_KEY not set! Run 'make setup' first$(RESET)"; \
		exit 1; \
	fi
	python src/assistant.py

clean: ## Clean up temporary files
	@echo "$(BLUE)🧹 Cleaning up...$(RESET)"
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
	@echo "$(GREEN)✅ Cleanup complete!$(RESET)"

test: ## Test the setup
	@echo "$(BLUE)🧪 Testing setup...$(RESET)"
	@python -c "import google.generativeai; print('✅ google-generativeai imported successfully')" || (echo "$(RED)❌ Dependencies missing, run 'make install'$(RESET)" && exit 1)
	@if [ -f "devlog.md" ]; then echo "$(GREEN)✅ Log file exists$(RESET)"; else echo "$(YELLOW)⚠️  No log file yet - run 'make log' to create one$(RESET)"; fi
	@if [ -n "$$GOOGLE_API_KEY" ]; then echo "$(GREEN)✅ API key configured$(RESET)"; else echo "$(YELLOW)⚠️  API key not set - run 'make setup' for instructions$(RESET)"; fi
	@echo "$(GREEN)🚀 Ready to go!$(RESET)"

# Development commands
dev-install: install ## Install development dependencies
	@echo "$(BLUE)📦 Installing development dependencies...$(RESET)"
	pip install pytest black flake8 mypy
	@echo "$(GREEN)✅ Development environment ready!$(RESET)"

format: ## Format code with black
	@echo "$(BLUE)🎨 Formatting code...$(RESET)"
	black src/
	@echo "$(GREEN)✅ Code formatted!$(RESET)"

lint: ## Lint code with flake8
	@echo "$(BLUE)🔍 Linting code...$(RESET)"
	flake8 src/
	@echo "$(GREEN)✅ Code linted!$(RESET)"

demo: ## Run a demo with sample data
	@echo "$(BLUE)🎭 Running demo...$(RESET)"
	cp examples/sample_log.md devlog.md
	@echo "$(GREEN)✅ Sample log loaded! Try 'make chat' to test the AI assistant$(RESET)"
