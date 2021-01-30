from django.db import models

class UserProfile(models.Model):
    """Database models for user in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TodoItem(models.Model):
    """Model for a single todo entry"""
    
    content = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    completed = models.BooleanField(default='False')

    def __str__(self):
        return self.content



