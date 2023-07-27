from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Candidate(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    created_on = models.DateTimeField(default=datetime.now())
    prefix = models.CharField(max_length=5)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    nationality = models.CharField(max_length = 25, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    isd_code = models.CharField(max_length=5, blank=True, null=True)
    mobile_no = models.CharField(max_length=15, blank = False)
    source = models.CharField(max_length=25, blank=False)
    source_category = models.CharField(max_length=20, blank=False)
    preferred_location = models.CharField(max_length=25, blank=False)
    current_ctc = models.BigIntegerField(blank=False)
    expected_ctc = models.BigIntegerField(blank=False)
    notice_period = models.IntegerField(blank=False)
    skills = models.TextField(max_length=200, default=None, blank=True, null=True)
    remarks = models.TextField(max_length=200, default=None, blank=True, null=True)
    pan_no = models.CharField(max_length=10, default=None, blank=True, null=True)
    aadhar_no = models.CharField(max_length=12, default=None, blank=True, null=True)
    passport_no = models.CharField(max_length=9, default=None, blank=True, null=True)
    expiry_date = models.DateField(default=None, blank=True, null=True)
    emergency_contact = models.CharField(max_length=15, default=None, blank=True, null=True)
    contact_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    relation = models.CharField(max_length=20, default=None, blank=True, null=True)
    current_address = models.TextField(max_length=250, default=None, blank=True, null=True)
    country = models.CharField(max_length=25, default=None, blank=True, null=True)
    state = models.CharField(max_length=25, default=None, blank=True, null=True)
    city = models.CharField(max_length=25, default=None, blank=True, null=True)
    pin_code = models.CharField(max_length=6, default=None, blank=True, null=True)
    assigned = models.BooleanField(default=False, blank=True, null=True)
    recruiter = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    last5feedback = models.TextField(default=None, blank=True, null=True)
    next_interview = models.DateField(default=None, blank=True, null=True)
    knockout_score = models.IntegerField(default=0, blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    position = models.CharField(max_length=30, blank=True, null=True)
    summary = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.middle_name:
            return(f"{self.first_name} {self.middle_name} {self.last_name}")
        else:
            return(f"{self.first_name} {self.last_name}")

class Education(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='education')
    degree = models.CharField(max_length=25)
    university = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class WorkExp(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='work_experiences')
    company_name = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    position = models.CharField(max_length=25)

    def __str__(self):
        return self.company_name

class Attachment(models.Model):
    created_on = models.DateTimeField(default=datetime.now())
    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=20)
    file = models.FileField(upload_to=r'C:\Users\anshu\OneDrive\Desktop\Work\test\core\files', default=None)

    def __str__(self):
        return self.name