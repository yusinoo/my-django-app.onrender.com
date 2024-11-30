# learning_logs/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if not User.objects.filter(username="your_username").exists():
        User.objects.create_superuser("your_username", "your_email@example.com", "your_password")
        print("Superuser created successfully!")
