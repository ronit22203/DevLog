#!/usr/bin/env python3
"""
Daily Logger - A script to log daily learnings, decisions, and concerns
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Add src directory to Python path
sys.path.insert(0, str(Path(__file__).parent))
from config import Config

def get_user_input():
    """Collect the three daily reflection inputs from the user"""
    print("DevLog - Daily Development Logger")
    print("=" * 40)
    print("Please answer the following questions:\n")
    
    # Get the three inputs with better prompting
    print("1. 📚 What did you learn today?")
    print("   (New technologies, concepts, debugging insights, etc.)")
    learning = input("   → ")
    
    print("\n2. 🚀 What decision did you make that moved your project/stack forward?")
    print("   (Architecture choices, tool selections, implementation decisions, etc.)")
    decision = input("   → ")
    
    print("\n3. 🤔 What are you unclear about? What's bothering you?")
    print("   (Technical challenges, bugs, design decisions, blockers, etc.)")
    unclear = input("   → ")
    
    return learning, decision, unclear

def format_entry(learning, decision, unclear):
    """Format the daily entry as markdown"""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M")
    
    entry = f"""
## {date_str} - Daily Log ({time_str})

### What I Learned Today
{learning}

### Decision That Moved My Project Forward
{decision}

### What I'm Unclear About / What's Bothering Me
{unclear}

---
"""
    return entry

def append_to_log_file(entry):
    """Append the entry to the markdown log file"""
    try:
        # Ensure log file exists
        Config.ensure_log_file_exists()
        log_file = Config.get_log_file()
        
        # Append the new entry
        with open(log_file, 'a', encoding='utf-8') as file:
            file.write(entry)
        
        print(f"\nEntry successfully logged to {log_file}")
        print("Use 'make chat' to analyze your logs with AI!")
        
    except Exception as e:
        print(f"\nError writing to file: {e}")

def main():
    """Main function to run the daily logging script"""
    try:
        # Get user inputs
        learning, decision, unclear = get_user_input()
        
        # Validate inputs (ensure not empty)
        if not any([learning.strip(), decision.strip(), unclear.strip()]):
            print("\nAll fields are empty! Please provide at least one response.")
            return
        
        # Format the entry
        entry = format_entry(learning, decision, unclear)
        
        # Save to file
        append_to_log_file(entry)
        
        print("\nThank you for logging your daily reflections!")
        print("Keep building, keep learning!")
        
    except KeyboardInterrupt:
        print("\n\nLogging cancelled. See you tomorrow!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
