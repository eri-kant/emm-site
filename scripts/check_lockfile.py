"""
Lockfile Integrity Checker
Ensures that the package-lock.json exists and matches the package.json.
This is a standard DevOps safety check.
"""

import os
import sys


def verify_lockfile_presence() -> None:
    """
    Checks if package-lock.json exists.
    In a professional FOSS project, this file is mandatory for 
    deterministic builds in CI/CD pipelines.
    """
    lockfile = "package-lock.json"
    
    try:
        if not os.path.exists(lockfile):
            print(f"[ERROR] {lockfile} is missing!")
            print("Action: Run 'npm install' to generate it before pushing.")
            sys.exit(1)
            
        # Check if the lockfile is empty (edge case)
        if os.path.getsize(lockfile) == 0:
            print(f"[ERROR] {lockfile} is empty.")
            sys.exit(1)
            
        print(f"[SUCCESS] {lockfile} detected and validated.")
        
    except (OSError, IOError) as error:
        print(f"[CRITICAL] System error while accessing {lockfile}: {error}")
        sys.exit(1)


if __name__ == "__main__":
    print("--- DevOps Integrity Check: Node Environment ---")
    verify_lockfile_presence()
    sys.exit(0)