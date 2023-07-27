from django.urls import path
from .views import CandidatesView, CandidateView

urlpatterns = [
    path('', CandidatesView.as_view(), name='get-or-add-candidates'), # GET, POST
    path('<int:pk>/', CandidateView.as_view(), name='get-update-candidate'), # GET, PUT
]