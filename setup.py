"""
Setup script for building standalone executables for Django app.
"""
import sys
import os
import shutil
from setuptools import setup

def clean_build_dirs():
    """Clean up build directories before starting."""
    dirs_to_clean = ['build', 'dist']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)

# Common configuration
COMMON_OPTIONS = {
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
}

if sys.platform == 'darwin':  # macOS
    # Clean build directories first
    clean_build_dirs()
    
    PYENV_PREFIX = os.path.expanduser('~/.pyenv/versions/3.11.0')
    PYTHON_FRAMEWORK = os.path.join(PYENV_PREFIX, 'lib', 'libpython3.11.dylib')
    
    if not os.path.exists(PYTHON_FRAMEWORK):
        raise ValueError(f"Python framework not found at {PYTHON_FRAMEWORK}")
    
    MAC_OPTIONS = COMMON_OPTIONS.copy()
    MAC_OPTIONS.update({
        'argv_emulation': True,
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
    })

    extra_options = dict(
        app=['launcher.py'],
        data_files=[],
        options={'py2app': MAC_OPTIONS},
        setup_requires=['py2app'],
    )

elif sys.platform == 'win32':  # Windows
    # Clean build directories first
    clean_build_dirs()
    
    WIN_OPTIONS = COMMON_OPTIONS.copy()
    WIN_OPTIONS.update({
        'windows': [{
            'script': 'launcher.py',
            'icon_resources': [(1, 'static/img/favicon.ico')],
        }],
        'data_files': [
            ('static', ['static/*']),
            ('templates', ['templates/*']),
            ('', ['.env']),
        ],
    })

    extra_options = dict(
        options={'py2exe': WIN_OPTIONS},
        setup_requires=['py2exe'],
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