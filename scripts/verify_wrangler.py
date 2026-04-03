"""
Wrangler JSON Validator.
Ensures the configuration is syntactically correct and contains 
the mandatory Cloudflare Pages fields.
"""

import json
import os
import sys

def validate_wrangler_config(file_path: str) -> None:
    """
    Validates the existence and structure of the wrangler configuration.
    """
    if not os.path.exists(file_path):
        print(f"[ERROR] Configuration file {file_path} not found.")
        sys.exit(1)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
            
            # Check for mandatory keys for a professional Astro deployment
            required_keys = ["name", "pages_build_output_dir"]
            for key in required_keys:
                if key not in config:
                    print(f"[ERROR] Missing mandatory key: '{key}'")
                    sys.exit(1)
            
            print(f"[SUCCESS] {file_path} is valid and ready for deployment.")
            
    except json.JSONDecodeError as err:
        print(f"[CRITICAL] JSON Syntax Error in {file_path}: {err}")
        sys.exit(1)

if __name__ == "__main__":
    print("--- Auditing Cloudflare Configuration ---")
    validate_wrangler_config("wrangler.json")