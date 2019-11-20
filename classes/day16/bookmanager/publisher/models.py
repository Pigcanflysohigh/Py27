from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=32)

class Book(models.Model):
    title = models.CharField(max_length=32)
    pub = models.ForeignKey('Publisher',on_delete=models.CASCADE)

