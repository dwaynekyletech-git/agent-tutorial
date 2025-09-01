#!/usr/bin/env python3

import datetime
from pathlib import Path

def generate_session_summary():
    """Generate a summary of the current coding session"""
    
    print("📊 Session Summary")
    print("=" * 40)
    
    # Check if session log exists
    log_file = Path(".claude/session-log.txt")
    
    if log_file.exists():
        print("📝 Session Activity:")
        
        # Count different types of activities
        with open(log_file, 'r') as f:
            lines = f.readlines()
        
        commands = [line for line in lines if line.startswith("Command:")]
        files_changed = [line for line in lines if line.startswith("Files changed:")]
        
        print(f"   • Commands executed: {len(commands)}")
        print(f"   • Files modified: {len(files_changed)}")
        
        if files_changed:
            print("\n📁 Files worked on:")
            for file_line in files_changed[-5:]:  # Show last 5
                files = file_line.replace("Files changed: ", "").strip()
                print(f"   • {files}")
    
    else:
        print("📝 No session activity logged yet")
    
    # Show current project status
    print(f"\n⏰ Session ended at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("🎯 Great work! Keep the momentum going!")

if __name__ == "__main__":
    generate_session_summary()