from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

class UserInfo(models.Model):
    description = models.CharField(max_length=250, blank=True, null=True)
    links = models.URLField(blank=True, null=True)