from django.urls import path
from .views import getJobsView

urlpatterns = [
    path('', getJobsView.as_view(), name='get-jobs'), # GET
]