from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import UserAccount, Setting

# Register your models here.

admin.site.register(UserAccount)
admin.site.register(Setting)

