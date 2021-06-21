from django.db import models

# Create your models here.

class Newsletter(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    subscribe = models.BooleanField(default=False)
    
    def __str__(self):
        return  self.name
