#!/usr/bin/env python3
"""
Configuration management for DevLog
"""

import os
from pathlib import Path

class Config:
    """Configuration class for DevLog"""
    
    # Default settings
    DEFAULT_LOG_FILE = "devlog.md"
    DEFAULT_MODEL = "gemini-1.5-flash"
    
    @classmethod
    def get_log_file(cls) -> str:
        """Get the log file path from environment or use default"""
        return os.getenv('DEVLOG_FILE', cls.DEFAULT_LOG_FILE)
    
    @classmethod
    def get_api_key(cls) -> str:
        """Get Google API key from environment"""
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY environment variable not found!\n"
                "Get your API key from: https://makersuite.google.com/app/apikey\n"
                "Then run: export GOOGLE_API_KEY='your-api-key-here'"
            )
        return api_key
    
    @classmethod
    def get_model_name(cls) -> str:
        """Get the AI model name from environment or use default"""
        return os.getenv('DEVLOG_MODEL', cls.DEFAULT_MODEL)
    
    @classmethod
    def ensure_log_file_exists(cls) -> None:
        """Create log file with header if it doesn't exist"""
        log_file = cls.get_log_file()
        if not os.path.exists(log_file):
            header = "# DevLog - Daily Development Log\n"
            header += "*A record of daily learnings, decisions, and reflections*\n\n"
            
            with open(log_file, 'w', encoding='utf-8') as file:
                file.write(header)
    
    @classmethod
    def get_project_root(cls) -> Path:
        """Get the project root directory"""
        return Path(__file__).parent.parent
