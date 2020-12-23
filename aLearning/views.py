from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'aLearning/index.html')
def courses(request):
    return render(request, 'aLearning/courses.html')
def course(request):
    return render(request, 'aLearning/course-single.html')
def panierVoir():
    return HttpResponse("Hello, world ! It is there I show cart content.")