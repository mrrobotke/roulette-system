"""Bootstrap module to handle package imports."""
import os
import sys

def bootstrap():
    """Set up the environment before running the main application."""
    # Add the Resources/lib/python3.12/site-packages to sys.path
    resources_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Resources')
    site_packages = os.path.join(resources_path, 'lib', 'python3.12', 'site-packages')
    sys.path.insert(0, site_packages)

    # Ensure packaging is available
    try:
        import packaging
    except ImportError:
        sys.stderr.write("Error: packaging module not found\n")
        sys.exit(1)

if __name__ == '__main__':
    bootstrap()