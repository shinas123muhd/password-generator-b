from django.db import models

# Create your models here.
class Passwords(models.Model):
    password =  models.CharField(max_length=20,null=False)
