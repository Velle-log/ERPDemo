
def valid_leave_application():
    pass

# @login_required(login_url='/accounts/login')
# def authority_check(request, id):
#
#     try:
#         application = ApplicationRequest.objects.get(id=id)
#
#     except:
#
#         return HttpResponse('Application does not exist !')
#
#     if application.recipient == request.user:
#
#         print('okay 1')
#
#         if application.leave.replacing_user == request.user:
#
#             print('is replacing user')
#
#             application.leave.application_status = 'processing'
#
#             try:
#
#                 if application.user.details.user_type == 'staff':
#
#                     des = Designation.objects.get(designation='Registrar', user_type='staff')
#                     hod = Designated.objects.filter(designation=des)[0]
#                     return
#                     # ApplicationRequest.objects.create(user=application.user, recipient=hod, leave=application.leave)
#                     # application.delete()
#                     #
#                     # return HttpResponse('success')
#
#                 else:
#
#                     des = Designation.objects.filter(designation='HOD', user_type='faculty')
#
#                     hods = Designated.objects.filter(designation=des)
#                     required_departement = application.user.details.department
#                     hod = list(filter(lambda x: x.user.details.department == required_departement, hods))[0].user
#
#                     ApplicationRequest.objects.create(user=application.user, recipient=hod, leave=application.leave)
#                     application.delete()
#
#                     return HttpResponse('success')
#
#             except Exception as e:
#                 return HttpResponse(e)#'HOD does not exist in database !')
#
#         else:
#             try:
#                 designation = request.user.designation.designation.designation
#             except:
#                 return HttpResponse('No Designations found')
#             # if request.user in Designated.objects.filter(user=request.user, designation=Designation.objects.get(designation='Director', user_type='faculty'))[0].user:
#             condition = request.user.details.department == application.user.details.department
#             if designation == 'HOD' and condition:
#                 application.leave.application_status = 'accepted'
#                 # ApplicationRequest.objects.create(user=application.user, recipient=hod, leave=application.leave)
#                 application.delete()
#
#                 return HttpResponse('success')
#
#             else:
#
#                 try:
#
#                     if application.user.details.user_type == 'staff':
#                         des = Designation.objects.get(designation='Registrar', user_type='staff')
#
#                     else:
#                         des = Designation.objects.get(designation='HOD', user_type='faculty')
#
#                 except:
#                     return HttpResponse('HOD does not exist in database !')
#
#                 if Designated.objects.filter(user=application.recipient, designation=des):
#
#                     hods = Designated.objects.filter(user=application.recipient, designation=des).values('user')
#
#                     if request.user in hods:
#                         application.leave.application_status = 'accepted'
#                         ApplicationRequest.objects.create(user=application.user, recipient=hod, leave=application.leave)
#                         application.delete()
#
#                         return HttpResponse('success')
#
#                     else:
#                         return HttpResponse('Unauthorised')
#                 else:
#                     return HttpResponse('Unauthorised')
#     else:
#         return HttpResponse('Unauthorised')
#
#
# @login_required(login_url = '/accounts/login')
# def reject_application(request, id):
#
#     try:
#         application = ApplicationRequest.objects.get(id=id)
#
#     except:
#
#         return HttpResponse('Application does not exist !')
#
#     if application.recipient == request.user:
#
#         print('okay 1')
#
#         if application.leave.replacing_user == request.user:
#
#             print('is replacing user')
#
#             application.leave.application_status = 'rejected'
#             try:
#                 application.delete()
#             except Exception as e:
#                 return HttpResponse(e)#'HOD does not exist in database !')
#
#         else:
#             try:
#                 designation = request.user.designation.designation.designation
#             except:
#                 return HttpResponse('No Designations found')
#             # if request.user in Designated.objects.filter(user=request.user, designation=Designation.objects.get(designation='Director', user_type='faculty'))[0].user:
#             condition = request.user.details.department == application.user.details.department
#             if designation == 'HOD' and condition:
#                 application.leave.application_status = 'rejected'
#                 # ApplicationRequest.objects.create(user=application.user, recipient=hod, leave=application.leave)
#                 application.delete()
#
#                 return HttpResponse('success')
#
#             else:
#
#                 try:
#
#                     if application.user.details.user_type == 'staff':
#                         des = Designation.objects.get(designation='Registrar', user_type='staff')
#
#                     else:
#                         des = Designation.objects.get(designation='HOD', user_type='faculty')
#
#                 except:
#                     return HttpResponse('HOD does not exist in database !')
#
#                 if Designated.objects.filter(user=application.recipient, designation=des):
#
#                     hods = Designated.objects.filter(user=application.recipient, designation=des).values('user')
#
#                     if request.user in hods:
#                         application.leave.application_status = 'rejected'
#                         application.delete()
#
#                         return HttpResponse('success')
#
#                     else:
#                         return HttpResponse('Unauthorised 1')
#                 else:
#                     return HttpResponse('Unauthorised 2')
#     else:
#         return HttpResponse('Unauthorised 3')
#
#
# @login_required(login_url='/accounts/login')
# def forward_application(request, id):
#
#     try:
#         application = ApplicationRequest.objects.get(id=id)
#
#     except:
#
#         return HttpResponse('Application does not exist !')
#
#     if application.recipient == request.user:
#
#         print('okay 1')
#
#         if application.leave.replacing_user == request.user:
#             return HttpResponse('Action unavailable')
#
#         else:
#             try:
#                 designation = request.user.designation.designation.designation
#             except:
#                 return HttpResponse('Authority related issue')
#             # if request.user in Designated.objects.filter(user=request.user, designation=Designation.objects.get(designation='Director', user_type='faculty'))[0].user:
#             if designation =='Director':
#                 return HttpResponse('Action unavailable')
#
#             else:
#
#                 try:
#
#                     if application.user.details.user_type == 'staff':
#                         des = Designation.objects.get(designation='Registrar', user_type='staff')
#
#                     else:
#                         des = Designation.objects.get(designation='HOD', user_type='faculty')
#
#                 except:
#                     return HttpResponse('HOD does not exist in database !')
#
#                 if Designated.objects.filter(user=application.recipient, designation=des):
#
#                     hods = Designated.objects.filter(user=application.recipient, designation=des)
#                     required_departement = application.user.details.department
#                     hod = list(filter(lambda x: x.user.details.department == required_departement, hods))[0].user
#                     print(hod)
#                     if request.user == hod:
#                         application.leave.application_status = 'processing'
#                         try:
#                             designation = Designation.objects.get(designation='Director')
#                             director = Designated.objects.get(designation=designation).user
#                         except Exception as e:
#                             return HttpResponse('Database Query errror- '+str(e) )
#                         ApplicationRequest.objects.create(user=application.user, recipient=director, leave=application.leave)
#                         application.delete()
#
#                         return HttpResponse('success')
#
#                     else:
#                         return HttpResponse('Unauthorised 1')
#                 else:
#                     return HttpResponse('Unauthorised 2')
#     else:
#         return HttpResponse('Unauthorised 3')
