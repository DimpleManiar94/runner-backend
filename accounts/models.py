from builtins import super

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone = models.CharField(max_length=10, blank=True)
    ProfilePicture = models.CharField(max_length=300, blank=True)
    Addr1 = models.CharField(max_length=200, blank=True)
    Addr2 = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=50, blank=True)
    State = models.CharField(max_length=50, blank=True)
    PostalCode = models.CharField(max_length=10, blank=True)

class Setting(models.Model):
    SETTINGS_TYPE = (
        ('Text', 'Text'),
        ('Push', 'Push Notification'),
        ('Email', 'Email'),
    )
    SETTINGS_STATUSES = (
        ('ON', 'ON'),
        ('OFF', 'OFF'),
    )
    UserFK = models.ForeignKey(UserAccount, on_delete=models.CASCADE, null=True)
    SettingsType = models.CharField(max_length=50, choices=SETTINGS_TYPE)
    TaskCompleted = models.CharField(max_length=3, choices=SETTINGS_STATUSES, default='ON')
    Likes = models.CharField(max_length=3, choices=SETTINGS_STATUSES, default='ON')
    Comments = models.CharField(max_length=3, choices=SETTINGS_STATUSES, default='ON')
    TaskPicked = models.CharField(max_length=3, choices=SETTINGS_STATUSES, default='ON')