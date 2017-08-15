from django import forms
from .models import Leave


class FacultyStaffLeave(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FacultyStaffLeave, self).__init__(*args, **kwargs)
        for field in self.fields:
            if 'date' not in field:
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Leave
        fields = ['type_of_leave', 'start_date', 'end_date', 'replacing_user', 'purpose', 'leave_address']
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),
        }
