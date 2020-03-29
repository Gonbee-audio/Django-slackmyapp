from django.db import models
from django.utils import timezone

# Create your models here.


class UserCreate(models.Model):
    username = models.CharField(max_length=255)
    text = models.TextField(max_length=255)
    images = models.ImageField(upload_to="")
    good = models.IntegerField(null=True, blank=True, default=0)
    def __str__(self):
        return self.username
