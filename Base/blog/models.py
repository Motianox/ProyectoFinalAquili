from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=40)
    subtitle = models.CharField(max_length=40)
    body = models.CharField(max_length=1000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    image = models.ImageField(upload_to='media', blank=True, null=True)
    def __str__(self):
        return f'{self.title} por {self.author}'
    