from django.shortcuts import render
from .models import Student

# Create your views here.
#add profile view

def profile(request):
    student = Student.objects.first()
    return render(request, 'student/profile.html', {'student': student})
