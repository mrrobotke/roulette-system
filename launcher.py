import os
import sys
import subprocess
import platform
import webbrowser
from pathlib import Path

def check_postgres():
    """Check if PostgreSQL is installed and running."""
    system = platform.system().lower()
    try:
        if system == 'windows':
            subprocess.run(['pg_isready'], check=True)
        else:
            subprocess.run(['pg_isready', '-q'])
        return True
    except:
        return False

def main():
    """Main launcher function."""
    # Set up environment variables
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'roulette_system_tracker.settings')
    
    # Database configuration
    os.environ['DB_NAME'] = 'roulette_db'
    os.environ['DB_USERNAME'] = 'roulette_user'
    os.environ['DB_PASSWORD'] = 'roulette123'
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_PORT'] = '5432'
    
    # Check PostgreSQL
    if not check_postgres():
        print("Error: PostgreSQL is not running!")
        print("Please install PostgreSQL and ensure it's running")
        input("Press Enter to exit...")
        sys.exit(1)

    # Start Django
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(['manage.py', 'migrate'])
        
        # Create superuser if it doesn't exist
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        
        # Start server and open browser
        print("Starting Roulette System Tracker...")
        webbrowser.open('http://localhost:8000')
        execute_from_command_line(['manage.py', 'runserver'])
        
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)

if __name__ == '__main__':
    main()