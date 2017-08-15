from django import forms
from .models import Department
try:
    DEPARTMENTS = ((dep, dep) for dep in Department.objects.all())
except:
    DEPARTMENTS = []
class SignupForm(forms.Form):

    CHOICES = (
        ('faculty', 'Faculty'),
        ('staff', 'Staff'),
        ('student', 'Student'),
    )


    department = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class': 'form-control'}), choices=DEPARTMENTS)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 30, 'class': 'form-control', 'placeholder': 'First Name'}), label='First Name')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'max_length': 50, 'class': 'form-control', 'placeholder': 'Last Name'}), label='Last Name')
    user_status = forms.ChoiceField(widget=forms.widgets.Select(attrs={'class':'form-control'}), choices=CHOICES)

    def signup(self, request, user):
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.extrainfo.department = Department.objects.get(
                    department_name=request.POST.get('department'))
        user.extrainfo.user_type = request.POST.get('user_status')
        user.extrainfo.save()
        user.save()
