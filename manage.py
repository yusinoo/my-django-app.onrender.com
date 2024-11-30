#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from django.contrib.auth.models import User

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
    try:
        # Import and create superuser
        from django.core.management import execute_from_command_line
        
        # Prepopulate superuser
        import django
        django.setup()  # Initialize Django
        if not User.objects.filter(username="your_username").exists():
            User.objects.create_superuser("your_username", "your_email@example.com", "your_password")
            print("Superuser created successfully!")
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
