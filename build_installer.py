"""Build standalone executable for the roulette system."""
import PyInstaller.__main__
import sys
import os
from pathlib import Path

def build_installer():
    """Build standalone executable for the roulette system."""
    
    # Get absolute paths
    BASE_DIR = Path(__file__).resolve().parent
    ICON_PATH = BASE_DIR / 'static' / 'img' / 'favicon.icns'
    
    # Verify icon exists
    if not ICON_PATH.exists():
        print(f"Warning: Icon file not found at {ICON_PATH}")
        print("Building without custom icon...")
    
    # Set Django settings before building
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roulette_system_tracker.settings')
    
    # Define build parameters
    build_params = [
        'launcher.py',  # Main script
        '--name=RouletteTracker',
        '--windowed',  # GUI mode
        '--noconfirm',
        '--clean',
        '--target-arch=arm64',  # Specifically for M1
        
        # Add icon if it exists
        f'--icon={ICON_PATH}' if ICON_PATH.exists() else None,
        
        # Add data files
        f'--add-data={BASE_DIR/"templates"}:templates',
        f'--add-data={BASE_DIR/"static"}:static',
        f'--add-data={BASE_DIR/"tracker"}:tracker',
        f'--add-data={BASE_DIR/"accounts"}:accounts',
        f'--add-data={BASE_DIR/"roulette_system_tracker"}:roulette_system_tracker',
        f'--add-data={BASE_DIR/".env"}:.env',
        
        # Add required packages
        '--hidden-import=django',
        '--hidden-import=django.template.defaulttags',
        '--hidden-import=django.template.defaultfilters',
        '--hidden-import=django.template.loader_tags',
        '--hidden-import=django.templatetags.static',
        '--hidden-import=django.contrib.messages.storage.fallback',
        '--hidden-import=django.contrib.staticfiles',
        '--hidden-import=django.contrib.admin',
        '--hidden-import=django.contrib.auth',
        '--hidden-import=django.contrib.contenttypes',
        '--hidden-import=django.contrib.sessions',
        '--hidden-import=django.contrib.messages',
        '--hidden-import=rest_framework',
        '--hidden-import=corsheaders',
        '--hidden-import=psycopg2',
        '--hidden-import=drf_yasg',
        '--hidden-import=packaging',
        
        # Runtime hooks
        '--runtime-hook=runtime_hooks.py',
    ]
    
    # Remove None values from build_params
    build_params = [param for param in build_params if param is not None]
    
    try:
        PyInstaller.__main__.run(build_params)
        print("Build completed successfully!")
    except Exception as e:
        print(f"Build failed with error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    build_installer()