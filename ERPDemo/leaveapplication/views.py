from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def get_applications(request):
    return HttpResponse('All the Leave requests will come here.')

def main_interface(request):
    return render(request, 'leaveapplication/main_interface.html')
