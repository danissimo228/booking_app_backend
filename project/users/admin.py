from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Users

admin.site.register(Users, UserAdmin)
