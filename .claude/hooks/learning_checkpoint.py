#!/usr/bin/env python3
"""
Learning Checkpoint Hook
Reminds you to ask questions during vibe coding sessions
"""

import os
import time

def learning_checkpoint():
    """Remind user to stay engaged in learning process"""
    
    # Check if significant code was just written
    claude_file_paths = os.environ.get('CLAUDE_FILE_PATHS', '')
    
    if claude_file_paths:
        print("🤔 Learning Checkpoint!")
        print("Files modified:", claude_file_paths)
        print("💡 Remember to ask:")
        print("   - Why was this approach chosen?")
        print("   - What alternatives existed?")
        print("   - How does this connect to bigger patterns?")
        print("   - Can I explain what was just built?")
        
        # Log the checkpoint
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open('.claude/checkpoints.log', 'a') as f:
            f.write(f"{timestamp} - Files modified: {claude_file_paths}\n")

if __name__ == "__main__":
    learning_checkpoint()