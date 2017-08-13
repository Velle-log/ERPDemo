from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def index(request):
    return HttpResponse('Welcome ' + request.user.username)
