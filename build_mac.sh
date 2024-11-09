#!/bin/bash

# Exit on error
set -e

echo "Building RouletteTracker for macOS..."

# Clean previous builds
rm -rf build dist

# Create and activate virtual environment
python3 -m venv venv_build
source venv_build/bin/activate

# Install requirements
pip install --upgrade pip
pip install -r requirements.txt

# Build the application
python build_installer.py

# Create DMG (optional)
if command -v create-dmg &> /dev/null; then
    echo "Creating DMG..."
    create-dmg \
        --volname "RouletteTracker" \
        --volicon "static/img/favicon.icns" \
        --window-pos 200 120 \
        --window-size 800 400 \
        --icon-size 100 \
        --icon "RouletteTracker.app" 200 190 \
        --hide-extension "RouletteTracker.app" \
        --app-drop-link 600 185 \
        "RouletteTracker.dmg" \
        "dist/RouletteTracker.app"
fi

echo "Build complete!"