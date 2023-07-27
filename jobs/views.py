from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import Job
from .serializers import getJobSerializer

# Create your views here.
class getJobsView(generics.ListAPIView):
    
    def get(self, request):
        queryset = Job.objects.all()
        serializer_class = getJobSerializer(queryset, many = True)
        return Response(serializer_class.data, status=200)