from django.contrib.auth.models import User
from django.db import models

class TODO(models.Model):

    title = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="user")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.user} -> {self.title}"
    
    
    