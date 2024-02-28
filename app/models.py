from django.db import models

# Create your models here.
class Post(models.Model):
    name_p = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)

class ee(models.Model):
    name_p = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=100,null=True)