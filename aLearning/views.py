from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'aLearning/courses.html')
def parcours(request):
    return render(request, 'aLearning/parcours-single.html')
def course(request):
    return render(request, 'aLearning/course-single.html')