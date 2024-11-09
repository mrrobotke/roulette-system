#!/usr/bin/env python
"""Django management script for roulette system tracker.

This script serves as the main entry point for Django management commands.
It configures the Django environment and executes management commands.
"""
import os
import sys
from pathlib import Path

def main():
    """Configure and execute Django management commands."""
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "roulette_system_tracker.settings")
        
        # Add the project root directory to Python path
        project_root = Path(__file__).resolve().parent
        sys.path.append(str(project_root))
        
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == "__main__":
    main()