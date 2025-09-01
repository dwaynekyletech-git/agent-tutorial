#!/usr/bin/env python3
"""
Learning Preparation Hook
Sets learning intentions before any tool use
"""

import os
import time

def learning_prep():
    """Prepare for learning before tool execution"""
    
    tool_name = os.environ.get('CLAUDE_TOOL_NAME', 'Unknown')
    
    print(f"🧠 Learning Mode: About to {tool_name}")
    
    # Different prep based on tool type
    if tool_name in ['Write', 'Edit', 'MultiEdit']:
        print("📝 Coding Prep Checklist:")
        print("   ✓ Do I understand WHY we're doing this?")
        print("   ✓ Have I considered the approach?")
        print("   ✓ Am I ready to ask follow-up questions?")
        
    elif tool_name == 'Bash':
        print("⚡ Command Prep Checklist:")
        print("   ✓ Do I understand what this command does?")
        print("   ✓ What output should I expect?")
        print("   ✓ How does this fit our workflow?")
        
    elif tool_name == 'Read':
        print("📖 Reading Prep:")
        print("   ✓ What am I looking for in this file?")
        print("   ✓ How will this inform our next step?")
        
    elif tool_name == 'Grep':
        print("🔍 Search Prep:")
        print("   ✓ What pattern am I looking for?")
        print("   ✓ How will the results guide our implementation?")
        
    elif tool_name == 'Glob':
        print("📂 File Discovery Prep:")
        print("   ✓ What files do I expect to find?")
        print("   ✓ How will this help understand the codebase?")
    
    else:
        print("🔧 Tool Prep:")
        print("   ✓ What's the purpose of this operation?")
        print("   ✓ How does this move us toward our goal?")
    
    # Log the preparation moment
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open('.claude/prep-log.txt', 'a') as f:
        f.write(f"{timestamp} - Prep for {tool_name}\n")

if __name__ == "__main__":
    learning_prep()