from django.contrib import admin

from .models import CustomUser, UserHobby, UserInterest

admin.site.register(CustomUser)
admin.site.register(UserHobby)
admin.site.register(UserInterest)