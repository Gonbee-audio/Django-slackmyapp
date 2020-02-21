from django.db import models

# Create your models here.


class Chat(models.Model):
    name = models.CharField(max_length=255, verbose_name='名前')

    chat_text = models.CharField(max_length=2000, verbose_name='TEXT')

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
