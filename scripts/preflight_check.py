"""
NASA EMM Project: Pre-flight Auditor
Validates the local WSL environment and project structure 
before pushing to Cloudflare Pages.
"""

import os
import sys
import subprocess

def check_command(command: str) -> bool:
    """Checks if a command-line tool is installed and accessible."""
    try:
        subprocess.run([command, "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def verify_environment() -> None:
    """Ensures Node.js and NPM are present in the WSL environment."""
    print("--- Checking System Dependencies ---")
    
    tools = ["node", "npm"]
    for tool in tools:
        if check_command(tool):
            print(f"[SUCCESS] {tool} is installed.")
        else:
            print(f"[ERROR] {tool} is missing. Install via: nvm install --lts")
            sys.exit(1)

def verify_project_structure() -> None:
    """
    Checks for the mandatory project files and warns about 
    conflicting Cloudflare configurations.
    """
    print("\n--- Auditing Project Structure ---")

    # 1. Check for package.json (The heartbeat of an Astro project)
    if not os.path.exists("package.json"):
        print("[ERROR] package.json not found. Run this script from the project root.")
        sys.exit(1)
    else:
        print("[SUCCESS] package.json verified.")

    # 2. Check for Wrangler Conflicts (Cloudflare Pages specific)
    # We want NO wrangler.json/toml because we configured the dashboard manually.
    wrangler_files = ["wrangler.json", "wrangler.toml"]
    conflict_found = False

    for f in wrangler_files:
        if os.path.exists(f):
            print(f"[WARNING] {f} detected. This may cause Cloudflare Pages build errors.")
            conflict_found = True

    if not conflict_found:
        print("[SUCCESS] No conflicting Wrangler files found. Clean for Pages deployment.")

def main():
    print("==========================================")
    print("   NASA EMM DEVOPS PRE-FLIGHT CHECK     ")
    print("==========================================\n")
    
    verify_environment()
    verify_project_structure()
    
    print("\n[RESULT] Pre-flight audit passed. You are cleared for deployment.")
    print("==========================================")

if __name__ == "__main__":
    main()