#!/usr/bin/env python3
"""
AI Assistant - Chat interface for your daily development logs
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent))
from config import Config

try:
    import google.generativeai as genai
except ImportError:
    print("google-generativeai package not found!")
    print("Install it with: pip install google-generativeai")
    print("Or run: make install")
    exit(1)

class DevLogAssistant:
    """AI assistant for analyzing development logs"""
    
    def __init__(self):
        """Initialize the assistant with API key and model"""
        try:
            self.api_key = Config.get_api_key()
            self.model_name = Config.get_model_name()
            self.log_file = Config.get_log_file()
            
            # Initialize Gemini
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel(self.model_name)
            
        except ValueError as e:
            print(f"Configuration error: {e}")
            exit(1)
        except Exception as e:
            print(f"Error initializing AI assistant: {e}")
            exit(1)
    
    def load_logs(self):
        """Load and return the content of the log file"""
        if not os.path.exists(self.log_file):
            print(f"Log file not found: {self.log_file}")
            print("Create your first entry with: make log")
            return None
        
        try:
            with open(self.log_file, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if not content.strip():
                print(f"Log file is empty: {self.log_file}")
                print("Create your first entry with: make log")
                return None
            
            return content
        except Exception as e:
            print(f"Error reading log file: {e}")
            return None
    
    def parse_entries(self, content):
        """Parse and count log entries"""
        date_pattern = r'^## (\d{4}-\d{2}-\d{2}) - Daily Log \((\d{2}:\d{2})\)$'
        sections = re.split(date_pattern, content, flags=re.MULTILINE)
        num_entries = (len(sections) - 1) // 3
        return num_entries
    
    def get_context_summary(self, content):
        """Get a summary of the log content for context"""
        num_entries = self.parse_entries(content)
        content_length = len(content)
        
        # Get recent entries (last 3000 characters for context)
        recent_content = content[-3000:] if len(content) > 3000 else content
        
        return {
            'num_entries': num_entries,
            'content_length': content_length,
            'recent_content': recent_content,
            'full_content': content
        }
    
    def generate_response(self, user_question, context):
        """Generate AI response based on user question and log context"""
        try:
            # Create an intelligent prompt
            prompt = f"""You are a helpful AI assistant analyzing a developer's daily log entries. 
The developer has been keeping track of their learnings, decisions, and challenges.

Context: The log contains {context['num_entries']} entries with {context['content_length']} characters total.

Recent log content:
{context['recent_content']}

User question: {user_question}

Please provide a helpful, insightful response based on the log content. Be specific and reference actual entries when relevant. If the question requires information not in the logs, say so politely.

Answer in a conversational, encouraging tone that helps the developer reflect on their progress."""

            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            error_msg = str(e)
            if "429" in error_msg or "quota" in error_msg.lower():
                return ("API quota exceeded! You've hit the daily limit.\n"
                       "Try again tomorrow or upgrade to a paid plan.\n"
                       "More info: https://ai.google.dev/gemini-api/docs/rate-limits")
            else:
                return f"Error generating response: {e}"
    
    def start_chat(self):
        """Start the interactive chat session"""
        print("DevLog AI Assistant v1.0")
        print("=" * 40)
        
        # Load logs
        content = self.load_logs()
        if not content:
            return False
        
        context = self.get_context_summary(content)
        
        print(f"Loaded {context['num_entries']} log entries ({context['content_length']} characters)")
        print(f"Using {self.model_name} model")
        
        print("\nChat with your development logs!")
        print("Examples:")
        print("   • 'What did I learn this week about React?'")
        print("   • 'What challenges have I been facing?'")
        print("   • 'Summarize my recent decisions'")
        print("   • 'What should I focus on next?'")
        print("\nType 'quit' to exit\n")
        
        # Chat loop
        while True:
            try:
                user_input = input("You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nThanks for using DevLog AI Assistant!")
                    print("Keep logging your journey with: make log")
                    break
                
                if not user_input:
                    continue
                
                print("Assistant: ", end="", flush=True)
                response = self.generate_response(user_input, context)
                print(f"{response}\n")
                
            except KeyboardInterrupt:
                print("\n\nChat interrupted. Keep building!")
                break
            except Exception as e:
                print(f"\nError: {e}")
        
        return True

def main():
    """Main function to start the assistant"""
    assistant = DevLogAssistant()
    assistant.start_chat()

if __name__ == "__main__":
    main()
