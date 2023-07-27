from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Job(models.Model):
    
    id = models.AutoField(primary_key=True, null=False)
    created_on = models.DateTimeField(default=datetime.now())
    
    designation = models.TextField(max_length=30)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    
    isTrending = models.BooleanField(default=False)
    
    min_exp = models.IntegerField(default=0)
    max_exp = models.IntegerField(default=0)
    
    assigned_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True, related_name='assigned_by')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True, related_name='assigned_to')
    
    starred = models.BooleanField(default=False)
    
    def __str__(self):
        return self.designation
    