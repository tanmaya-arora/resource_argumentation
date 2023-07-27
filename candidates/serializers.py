from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Candidate, WorkExp, Education, Attachment

User = get_user_model()

class RecruiterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'email',
            'name',
            'phone',
        )

class WorkExpSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkExp
        fields = (
            'company_name',
            'start_date',
            'end_date',
            'position',
        )

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            'degree',
            'university',
            'start_date',
            'end_date',
        )

class CandidatesSerializer(serializers.ModelSerializer):

    work_experiences = WorkExpSerializer(many = True, read_only = True)
    recruiter = RecruiterSerializer(many=False, read_only = True)
    education = EducationSerializer(many = True, read_only = True)

    class Meta:
        model = Candidate
        fields = (
            'id',
            'first_name',
            'middle_name',
            'last_name',
            'work_experiences',
            'next_interview',
            'last5feedback',
            'knockout_score',
            'recruiter',
            'source',
            'source_category',
            'rating',
            'education',
        )

class CandidateSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    work_experiences = WorkExpSerializer(many=True, read_only = True)
    education = EducationSerializer(many=True, read_only = True)
    recruiter = RecruiterSerializer(many=False, read_only = True)

    class Meta:
        model = Candidate
        fields = (
            'name',
            'work_experiences',
            'mobile_no',
            'education',
            'position',
            'recruiter',
            'source',
            'source_category',
            'current_address',
            'email',
            'summary',
        )

    def get_name(self, obj):
        return f"{obj.first_name} {obj.middle_name} {obj.last_name}" if obj.middle_name else f"{obj.first_name} {obj.last_name}"
