from django.contrib import admin
from .models import Candidate, WorkExp, Education

admin.site.register(Candidate)
admin.site.register(WorkExp)
admin.site.register(Education)