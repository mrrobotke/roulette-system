"""Runtime hooks for PyInstaller."""
import os
import sys
from pathlib import Path

def setup_environment():
    """Set up the environment for the frozen application."""
    if getattr(sys, 'frozen', False):
        # Running in a bundle
        base_dir = Path(sys._MEIPASS)
        
        # Add necessary paths
        sys.path.insert(0, str(base_dir))
        
        # Set environment variables
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roulette_system_tracker.settings')
        os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
        
        # Set up Django paths
        os.environ['DJANGO_STATIC_ROOT'] = str(base_dir / 'static')
        os.environ['DJANGO_TEMPLATE_ROOT'] = str(base_dir / 'templates')

setup_environment()