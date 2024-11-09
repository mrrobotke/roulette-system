"""
Setup script for building standalone executables.
Handles both py2app (Mac) and cx_Freeze (Windows) builds.
"""
import sys
import os
from setuptools import setup
import cx_Freeze

# Determine the platform
is_mac = sys.platform == 'darwin'
is_win = sys.platform == 'win32'

# Common data files to include
DATA_FILES = [
    ('templates', ['templates/']),
    ('static', ['static/']),
    ('tracker', ['tracker/']),
    ('accounts', ['accounts/']),
    ('roulette_system_tracker', ['roulette_system_tracker/']),
]

if is_mac:
    from setuptools import setup
    
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
        ],
        'includes': [
            'django.template.defaulttags',
            'django.template.defaultfilters',
            'django.template.loader_tags',
            'django.templatetags.static',
            'django.contrib.messages.storage.fallback',
        ],
        'iconfile': 'static/img/favicon.icns',  # Make sure to convert your .ico to .icns for Mac
        'plist': {
            'CFBundleName': 'RouletteTracker',
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleVersion': '1.0.0',
            'CFBundleIdentifier': 'com.yourdomain.roulettetracker',
            'NSHighResolutionCapable': True,
        }
    }
    
    extra_options = dict(
        app=['run_django.py'],
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )

elif is_win:
    from cx_Freeze import setup, Executable
    
    build_exe_options = {
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
        ],
        'includes': [
            'django.template.defaulttags',
            'django.template.defaultfilters',
            'django.template.loader_tags',
            'django.templatetags.static',
            'django.contrib.messages.storage.fallback',
        ],
        'include_files': DATA_FILES,
        'excludes': ['tkinter', 'test', 'distutils'],
    }
    
    extra_options = dict(
        executables=[
            Executable(
                'run_django.py',
                base='Win32GUI',
                target_name='RouletteTracker.exe',
                icon='static/img/favicon.ico',
            )
        ],
        options={'build_exe': build_exe_options}
    )

else:
    print("Unsupported platform")
    sys.exit(1)

setup(
    name='RouletteTracker',
    version='1.0',
    description='Roulette System Tracker',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://yourdomain.com',
    **extra_options
)