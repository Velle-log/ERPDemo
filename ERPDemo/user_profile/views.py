from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/accounts/login')
def index(request):
    return render(request, 'user_profile/home.html')

@login_required(login_url='/accounts/login')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile/profile.html', {'user':user})
