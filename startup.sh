#!/bin/bash

echo "🚀 Starting Roulette System Setup..."

# Check operating system
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS setup
    if ! command -v brew &> /dev/null; then
        echo "Installing Homebrew..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    
    if ! command -v postgres &> /dev/null; then
        echo "Installing PostgreSQL..."
        brew install postgresql@15
    fi

    # Start PostgreSQL
    brew services start postgresql@15
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux setup
    if ! command -v psql &> /dev/null; then
        echo "Installing PostgreSQL..."
        sudo apt-get update
        sudo apt-get install -y postgresql postgresql-contrib
    fi
    
    # Start PostgreSQL
    sudo service postgresql start
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    # Windows setup
    echo "Please ensure PostgreSQL is installed from https://www.postgresql.org/download/windows/"
    echo "And ensure it's running in Services"
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating Python virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
source venv/bin/activate 2>/dev/null || source venv/Scripts/activate 2>/dev/null

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Database configuration variables
DB_NAME="roulette_db"
DB_USER="roulette_user"
DB_PASSWORD="roulette123"

# Setup database
echo "Setting up database..."
psql postgres -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASSWORD' CREATEDB;" 2>/dev/null
psql postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;" 2>/dev/null

# Update local settings
echo "Configuring local settings..."
mkdir -p roulette_system_tracker
cat > roulette_system_tracker/settings_local.py << EOF
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '$DB_NAME',
        'USER': '$DB_USER',
        'PASSWORD': '$DB_PASSWORD',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
EOF

# Setup Django
echo "Setting up Django..."
python manage.py migrate
python manage.py collectstatic --noinput

# Create default superuser
python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin123') if not User.objects.filter(username='admin').exists() else None"

# Start application
echo "🎲 Starting Roulette System Tracker..."
python manage.py runserver
