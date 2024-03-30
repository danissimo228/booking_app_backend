from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Users

# admin.site.register(Users, UserAdmin)


@admin.register(Users)
class RouteAdmin(admin.ModelAdmin):
    display_fields = (
        'phone', 'gender', 'geolocation', 'rating', 'photo', 'date_of_birthday', 'is_staff', 'is_active'
    )
