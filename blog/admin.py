# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Django now knows to display our blog app and its
# database model Post on the admin panel
