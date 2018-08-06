from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.DO_NOTHING,)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)