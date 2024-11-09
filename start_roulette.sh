#!/bin/bash
echo "🎲 Starting Roulette System Tracker..."

# Clone the main repository if it doesn't exist
if [ ! -d "roulette-system" ]; then
    echo "Downloading Roulette System..."
    git clone https://github.com/mrrobotke/roulette-system.git
    cd roulette-system
else
    cd roulette-system
    git pull
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed! Please install Python 3.8 or higher."
    echo "Download from: https://www.python.org/downloads/"
    exit 1
fi

# Check if PostgreSQL is installed
if ! command -v psql &> /dev/null; then
    echo "PostgreSQL is not installed! Please install PostgreSQL 15."
    echo "Download from: https://www.postgresql.org/download/macos/"
    exit 1
fi

# Create and activate virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Start the application
./startup.sh 