from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserAccount(AbstractUser):
    Phone = models.CharField(max_length=10)
    ProfilePicture = models.CharField(max_length=300, blank=True)
    Addr1 = models.CharField(max_length=200)
    Addr2 = models.CharField(max_length=200, blank=True)
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    PostalCode = models.CharField(max_length=10)

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