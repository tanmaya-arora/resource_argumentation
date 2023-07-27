from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CandidatesSerializer, CandidateSerializer
from .models import Candidate

# Create your views here.

class CandidateView(generics.RetrieveUpdateAPIView):
    
    @classmethod
    def get(cls, request, pk):
        candidate = Candidate.objects.get(id=pk)
        serializer_class = CandidateSerializer(candidate, many=False)
        return Response(serializer_class.data, status=200)
    
    @classmethod
    def put(cls, request, pk):
        candidate = Candidate.objects.get(id=pk)
        data = request.data
        
        candidate.prefix = data.get('prefix')
        candidate.first_name = data.get('first_name')
        candidate.middle_name = data.get('middle_name')
        candidate.last_name = data.get('last_name')
        candidate.date_of_birth = data.get('date_of_birth')
        candidate.gender = data.get('gender')
        candidate.nationality = data.get('nationality')
        candidate.email = data.get('email')
        candidate.isd_code = data.get('isd_code')
        candidate.mobile_no = data.get('mobile_no')
        candidate.source = data.get('source')
        candidate.source_category = data.get('source_category')
        candidate.preferred_location = data.get('preferred_location')
        candidate.current_ctc = data.get('current_ctc')
        candidate.expected_ctc = data.get('expected_ctc')
        candidate.notice_period = data.get('notice_period')
        candidate.skills = data.get('skills')
        candidate.remarks = data.get('remarks')
        candidate.pan_no = data.get('pan_no')
        candidate.aadhar_no = data.get('aadhar_no')
        candidate.passport_no = data.get('passport_no')
        candidate.expiry_date = data.get('expiry_date')
        candidate.emergency_contact = data.get('emergency_contact')
        candidate.contact_name = data.get('contact_name')
        candidate.relation = data.get('relation')
        candidate.current_address = data.get('current_address')
        candidate.country = data.get('country')
        candidate.state = data.get('state')
        candidate.city = data.get('city')
        candidate.pin_code = data.get('pin_code')
        
        candidate.save()
        
        serializer = CandidateSerializer(candidate, many=False)
        return Response(serializer.data, status=200)

# class CandidateView(generics.RetrieveUpdateAPIView):
#     pass


class CandidatesView(generics.ListCreateAPIView):
    
    def get(self, request):
        candidates = Candidate.objects.all()
        serializer = CandidatesSerializer(candidates, many=True, context={'request': request})
        return Response(serializer.data, status=200)

    def post(self, request):
        recruiter = request.user
        data = request.data
        candidate = Candidate.objects.create(
            prefix = data.get('prefix'),
            middle_name = data.get('middle_name'),
            last_name = data.get('last_name'),
            date_of_birth = data.get('date_of_birth'),
            gender = data.get('gender'),
            nationality = data.get('nationality'),
            email = data.get('email'),
            isd_code = data.get('isd_code'),
            mobile_no = data.get('mobile_no'),
            source = data.get('source'),
            source_category = data.get('source_category'),
            preferred_location = data.get('preferred_location'),
            current_ctc = data.get('current_ctc'),
            expected_ctc = data.get('expected_ctc'),
            notice_period = data.get('notice_period'),
            skills = data.get('skills'),
            remarks = data.get('remarks'),
            pan_no = data.get('pan_no'),
            aadhar_no = data.get('aadhar_no'),
            passport_no = data.get('passport_no'),
            expiry_date = data.get('expiry_date'),
            emergency_contact = data.get('emergency_contact'),
            contact_name = data.get('contact_name'),
            relation = data.get('relation'),
            current_address = data.get('current_address'),
            country = data.get('country'),
            state = data.get('state'),
            city = data.get('city'),
            pin_code = data.get('pin_code'),
            recruiter = recruiter
        )

        serializer = CandidateSerializer(candidate, many=False)
        return Response(serializer.data, status=201)