from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Job
from candidates.serializers import RecruiterSerializer

User = get_user_model()

class getJobSerializer(serializers.ModelSerializer):
    
    assigned_to = RecruiterSerializer(many = False, read_only = True)
    assigned_by = RecruiterSerializer(many = False, read_only = True)
    
    class Meta:
        model = Job
        fields = (
            'id',
            'created_on',
            'designation',
            'city',
            'state',
            'country',
            'isTrending',
            'min_exp',
            'max_exp',
            'assigned_by',
            'assigned_to',
            'starred'
        )