#!/usr/bin/env python
"""
Launcher script for the Roulette System Tracker.
Handles environment setup and application startup.
"""
import os
import sys
from pathlib import Path

def main():
    """Main entry point for the application."""
    try:
        # Set up Django environment
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roulette_system_tracker.settings')
        
        # Add the project directory to Python path
        if getattr(sys, 'frozen', False):
            # Running in a bundle
            base_dir = Path(sys._MEIPASS)
            # Ensure sys.argv has at least one element for the autoreloader
            if not sys.argv:
                sys.argv.append('')
        else:
            # Running in normal Python environment
            base_dir = Path(__file__).resolve().parent
        
        sys.path.insert(0, str(base_dir))
        
        # Initialize Django
        import django
        django.setup()
        
        # Disable autoreload in frozen environment
        if getattr(sys, 'frozen', False):
            os.environ['DJANGO_AUTORELOAD'] = 'false'
            from django.core.management import execute_from_command_line
            execute_from_command_line(['', 'runserver', '127.0.0.1:8000', '--noreload'])
        else:
            from django.core.management import execute_from_command_line
            execute_from_command_line(['', 'runserver', '127.0.0.1:8000'])
        
    except Exception as e:
        import traceback
        error_msg = f"Error starting application: {str(e)}\n{traceback.format_exc()}"
        sys.stderr.write(error_msg)
        sys.exit(1)

if __name__ == '__main__':
    main()