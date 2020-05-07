from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Content(models.Model):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 500)

class Comment(models.Model):
    post = models.ForeignKey('Content', on_delete=models.CASCADE)
    text = models.TextField(default='')