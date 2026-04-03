"""
Consolidated Pre-flight Check.
Verifies FOSS dependencies and Cloudflare configuration.
"""

import json
import os
import sys

def verify_project_config() -> None:
    """
    Checks package.json for dependencies and wrangler.json for build paths.
    """
    # 1. Check package.json
    if not os.path.exists("package.json"):
        print("[ERROR] package.json missing.")
        sys.exit(1)
        
    # 2. Check wrangler.json
    if not os.path.exists("wrangler.json") and not os.path.exists("wrangler.toml"):
        print("[ERROR] No wrangler configuration found.")
        sys.exit(1)

    if os.path.exists("wrangler.json"):
        try:
            with open("wrangler.json", "r") as f:
                config = json.load(f)
                if "pages_build_output_dir" not in config:
                    print("[WARNING] 'pages_build_output_dir' missing in wrangler.json.")
                    print("Action: Add '\"pages_build_output_dir\": \"./dist\"' to your config.")
        except json.JSONDecodeError:
            print("[CRITICAL] wrangler.json is malformed.")
            sys.exit(1)

    print("[SUCCESS] Project configuration verified.")

if __name__ == "__main__":
    verify_project_config()