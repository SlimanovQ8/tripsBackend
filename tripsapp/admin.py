from django.contrib import admin

# Register your models here.
from .models import UserProfile, Trips, User
admin.site.register(UserProfile)
admin.site.register(Trips)