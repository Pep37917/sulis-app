from django.db import models

# Create your models here.

class Bin(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f"Name: {self.name}"