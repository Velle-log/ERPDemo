from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .helpers import valid_leave_application


from .forms import FacultyStaffLeave

# Create your views here.
@login_required(login_url='/accounts/login')
def get_applications(request):
    return HttpResponse('All the Leave requests will come here.')

@login_required(login_url='/accounts/login')
def main_interface(request):

    if request.method == 'POST':
        form = FacultyStaffLeave(request.POST)
        if form.is_valid():
            return render(request, 'leaveapplication/apply.html')
        return render(request, 'leaveapplication/apply.html')
    form = FacultyStaffLeave(initial={})
    # response = render_to_string('leaveapplication/application_form.html', request=request, context={'form': form})
    # return JsonResponse({'data': response, 'other': 'otherdata'})
    return render(request, 'leaveapplication/application_form.html', {'form': form})
