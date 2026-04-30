#!/usr/bin/env python
"""
Run once to create the admin superuser.
Usage: python create_superuser.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

username = 'admin'
email    = 'ABCSuccessLab@gmail.com'
password = 'ABCAdmin2026!'   # CHANGE THIS immediately after first login

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f'Superuser created: {username} / {password}')
    print('IMPORTANT: Change the password at /admin/ after first login.')
else:
    print(f'Superuser "{username}" already exists.')
