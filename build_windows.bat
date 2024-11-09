@echo off
echo Building RouletteTracker for Windows...

:: Clean previous builds
rmdir /s /q build dist

:: Create and activate virtual environment
python -m venv venv_build
call venv_build\Scripts\activate

:: Install requirements
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install py2exe

:: Build the application
python build_installer.py

:: Create installer (optional)
:: You might want to use NSIS or Inno Setup here

echo Build complete!