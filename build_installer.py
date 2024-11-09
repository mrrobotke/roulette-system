import PyInstaller.__main__
import sys
import os

def build_installer():
    """Build standalone executable for the roulette system."""
    
    # Set Django settings before building
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roulette_system_tracker.settings')
    
    # Define build parameters
    build_params = [
        'run_django.py',
        '--name=RouletteTracker',
        '--onedir',
        '--windowed',
        '--noconfirm',  # Skip confirmation prompts
        '--clean',  # Clean PyInstaller cache
        
        # Add data files
        '--add-data=templates:templates',
        '--add-data=static:static',
        '--add-data=tracker:tracker',
        '--add-data=accounts:accounts',
        '--add-data=roulette_system_tracker:roulette_system_tracker',
        
        # Add required imports
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
        
        # For Mac, specify the target architecture
        '--target-arch=universal2',
        
        # Remove icon specification since it's causing issues
        # '--icon=static/img/favicon.ico',
    ]
    
    try:
        PyInstaller.__main__.run(build_params)
        print("Build completed successfully!")
    except Exception as e:
        print(f"Build failed with error: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    build_installer()