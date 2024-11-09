"""
Setup script for building standalone executables for Django app.
"""
import sys
import os
import shutil
from setuptools import setup

# Determine the platform
is_mac = sys.platform == 'darwin'

# Get absolute paths for data files
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Get the pyenv Python path (this should be set before venv activation)
PYENV_PREFIX = os.path.expanduser('~/.pyenv/versions/3.11.0')

def clean_build_dirs():
    """Clean up build directories before starting."""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

if is_mac:
    # Clean build directories first
    clean_build_dirs()
    
    # Get the Python framework path for pyenv installation
    PYTHON_FRAMEWORK = os.path.join(
        PYENV_PREFIX,
        'lib',
        'libpython3.11.dylib'
    )
    
    if not os.path.exists(PYTHON_FRAMEWORK):
        raise ValueError(f"Python framework not found at {PYTHON_FRAMEWORK}")
    
    OPTIONS = {
        'argv_emulation': True,
        'packages': [
            'django',
            'rest_framework',
            'corsheaders',
            'psycopg2',
            'drf_yasg',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'tracker',
            'accounts',
            'roulette_system_tracker',
        ],
        'includes': [
            'packaging',
            'packaging.version',
            'packaging.specifiers',
            'packaging.requirements',
            'pkg_resources',
        ],
        'excludes': [
            'matplotlib',
            'numpy',
            'PIL',
        ],
        'frameworks': [PYTHON_FRAMEWORK],
        'resources': ['static', 'templates', '.env'],
        'iconfile': 'static/img/favicon.icns',
        'plist': {
            'CFBundleName': 'RouletteTracker',
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleVersion': '1.0.0',
            'CFBundleIdentifier': 'com.yourdomain.roulettetracker',
            'NSHighResolutionCapable': True,
            'LSMinimumSystemVersion': '10.13',
        },
        'site_packages': True,
        'semi_standalone': False,
        'alias': False,
        'strip': False,
    }

    extra_options = dict(
        app=['launcher.py'],
        data_files=[],
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )

else:
    print("Unsupported platform")
    sys.exit(1)

setup(
    name='RouletteTracker',
    version='1.0',
    description='Roulette System Tracker',
    author='Appollan',
    author_email='support@appollan.com',
    url='https://appollan.com',
    **extra_options
)