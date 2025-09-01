#!/usr/bin/env python3
"""
TypeScript Learning Quality Checker
Runs type checking and explains any issues for learning
"""

import subprocess
import sys
import os

def check_typescript_quality():
    """Run TypeScript checks and provide learning feedback"""
    
    print("🔍 Checking TypeScript quality for learning...")
    
    # Run TypeScript compiler check
    try:
        result = subprocess.run(['npx', 'tsc', '--noEmit'], 
                              capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print("✅ TypeScript compilation successful!")
            print("💡 Great! All types are properly defined.")
        else:
            print("🚨 TypeScript issues found - Learning opportunity!")
            print("Error details:", result.stderr)
            print("\n💭 Ask Claude Code to explain these type errors!")
            
    except subprocess.TimeoutExpired:
        print("⏰ TypeScript check timed out")
    except FileNotFoundError:
        print("📦 TypeScript not found - make sure it's installed")

if __name__ == "__main__":
    check_typescript_quality()