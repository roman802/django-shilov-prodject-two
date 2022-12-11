from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Diskus(models.Model):
    
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    detecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title