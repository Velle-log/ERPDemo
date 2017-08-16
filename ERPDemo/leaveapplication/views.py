from django.shortcuts import render
from django.template.loader import render_to_string
from django.template import RequestContext
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .helpers import valid_leave_application
from .forms import FacultyStaffLeave, StudentLeave
from .models import Leave, ApplicationRequest, RemainingLeaves
from user_profile.models import Designated, Designation
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404

# Create your views here.

#To get all the application requests pending for the current user
@login_required(login_url='/accounts/login')
def get_applications(request):
    if request.user.application_request.all().count() != 0:
        applications = request.user.application_request.all()
        return render(request, 'leaveapplication/application_request.html', {'user': request.user, 'applications':applications})
    return HttpResponse('No Pending Requests')



@login_required(login_url='/accounts/login')
def process_request(request, id):

    application = get_object_or_404(ApplicationRequest, id=id)
    processing_status = application.leave.processing_status
    if request.method == 'GET':

        to_do = request.GET.get('action')
        required_departement = application.user.details.department

        if to_do == 'reject' and request.user == application.recipient:

            application.application_status = 'rejected'
            application.delete()
            return HttpResponse('Application Rejected')

        elif to_do == 'accept':

            if request.user == application.leave.replacing_user \
                and processing_status == 'rep user':

                if required_departement == 'None':
                    designation = Designation.objects.get(designation='Registrar')
                    next_recipient = Designated.objects.get(designation=designation)
                    required_designation = 'Registrar'

                else:
                    designation = Designation.objects.get(designation='HOD')
                    hods = Designated.objects.filter(designation=designation)
                    next_recipient = list(filter(lambda x: x.user.details.department == required_departement, hods))[0].user
                    required_designation = 'HOD'

                application.recipient = next_recipient
                application.leave.processing_status = required_designation
                application.save()
                application.leave.save()

            else:
                try:
                    designation = request.user.designation.designation
                except:
                    return HttpResponse('You are not allowed to do this.')

                condition = (                                                                           \
                                designation.designation == 'HOD'                                        \
                                and request.user.details.department == required_departement             \
                                and processing_status == 'HOD'                                          \
                            )                                                                           \
                            or                                                                          \
                            (                                                                           \
                                designation.designation == 'Director'                                   \
                                and processing_status == 'Director'                                     \
                            )                                                                           \
                            or                                                                          \
                            (                                                                           \
                                designation.designation == 'Registrar'                                  \
                                and processing_status == 'Registrar'                                    \
                            )

                if condition:
                    application.leave.application_status = 'accepted'
                    application.leave.save()
                    application.delete()

        else:
            designation = request.user.designation.designation
            condition = designation.designation == 'HOD'                                        \
                        and request.user.details.department == required_departement             \
                        and processing_status == 'HOD'
            print(designation.designation, request.user.details.department, required_departement, processing_status)
            if condition:
                designation = Designation.objects.get(designation='Director')
                next_recipient = Designated.objects.get(designation=designation).user
                application.recipient = next_recipient
                application.leave.processing_status = 'Director'
                application.save()
                application.leave.save()

            else:
                return HttpResponse('You are not allowed to do this')

        return HttpResponse('Done')


@login_required(login_url='/accounts/login')
def main_interface(request):

    if request.method == 'POST':
        if request.user.details.user_type == 'student':
            form = StudentLeave(request.POST)
        else:
            form = FacultyStaffLeave(request.POST, user=request.user)

        if form.is_valid():

            if request.user.details.user_type == 'student':
                type_of_leave = 'station_leave'
                designation = Designation.objects.get(designation='HOD')
                hods = Designated.objects.filter(designation=designation)
                required_departement = request.user.details.department
                replacing_user = list(filter(lambda x: x.user.details.department == required_departement, hods))[0].user
                processing_status = 'HOD'

            else:
                replacing_user = User.objects.get(username=form.cleaned_data['replacing_user'])
                type_of_leave = form.cleaned_data['type_of_leave']
                processing_status = 'rep user'

            print(processing_status)
            leave = Leave.objects.create(
                applicant = request.user,
                replacing_user = replacing_user,
                type_of_leave = type_of_leave,
                start_date = form.cleaned_data['start_date'],
                end_date = form.cleaned_data['end_date'],
                purpose = form.cleaned_data['purpose'],
                leave_address = form.cleaned_data['leave_address'],
                processing_status = processing_status,
            )

            ApplicationRequest.objects.create(
                user = request.user,
                recipient = replacing_user,
                leave = leave,
            )

            return render(request, 'leaveapplication/apply.html')
        errors = [ value for key, value in form.errors.items() ]
        return render(request, 'leaveapplication/apply.html', {'form': form, 'errors': errors})

    if request.user.details.user_type == 'student':
        form = StudentLeave(initial={})
    else:
        form = FacultyStaffLeave(initial={})

    return render(request, 'leaveapplication/application_form.html', {'form': form})
