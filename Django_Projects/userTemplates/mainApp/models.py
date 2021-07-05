from django.db import models

class user(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    age = models.IntegerField(default=0)
