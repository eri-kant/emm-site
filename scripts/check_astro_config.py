"""
Astro Configuration Auditor.
Verifies that the Tailwind integration is present in the Astro config file.
"""
import os
import sys

def verify_tailwind_integration(config_path: str) -> None:
    """
    Scans the astro.config.mjs for the tailwind() integration call.
    
    Args:
        config_path (str): Path to the Astro configuration file.
    """
    if not os.path.exists(config_path):
        print(f"[CRITICAL] Configuration file {config_path} not found.")
        sys.exit(1)

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Check for the tailwind import and the integration call
            has_import = 'import tailwind from "@astrojs/tailwind"' in content or "import tailwind from '@astrojs/tailwind'" in content
            has_integration = "tailwind()" in content
            
            if has_import and has_integration:
                print(f"[SUCCESS] Astro is correctly configured to use Tailwind in {config_path}.")
            else:
                print(f"[ERROR] Tailwind integration is missing or malformed in {config_path}.")
                print("Action: Ensure your config includes: integrations: [tailwind()]")
                sys.exit(1)
                
    except (IOError, OSError) as err:
        print(f"[SYSTEM ERROR] Could not read config: {err}")
        sys.exit(1)

if __name__ == "__main__":
    PATH = "astro.config.mjs"
    print(f"--- Auditing {PATH} for DevOps Compliance ---")
    verify_tailwind_integration(PATH)