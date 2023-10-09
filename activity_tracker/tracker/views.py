from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def Main(request):
   return render(request,'Main.html')

def LoginStudent(request):
  return render(request, 'LoginStudent.html')

def LoginMentor(request):
  return render(request, 'LoginMentor.html')

def HomeMentor(request):
  return render(request, 'HomeMentor.html')

def activitypoints(request):
  return render(request, 'activitypoints.html')

def saishruthi(request):
  return render(request, 'saishruthi.html')

def notifications(request):
  return render(request, 'notifications.html')