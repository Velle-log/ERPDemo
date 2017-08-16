from django import forms
from .models import Leave
from datetime import datetime

class FacultyStaffLeave(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        if 'user' in kwargs.keys():
            self.user = kwargs.pop('user')

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

    def clean_end_date(self):

        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']
        if start_date > end_date or start_date.strftime("%m/%d/%Y") < datetime.now().strftime("%m/%d/%Y"):
            raise forms.ValidationError('Invalid Dates Entered')
        return start_date

    def clean_replacing_user(self):
        replacing_user = self.cleaned_data['replacing_user']
        if replacing_user == self.user:
            raise forms.ValidationError('Can\'t choose yourself as replacing user')
        return replacing_user

    def clean_leave_address(self):

        if self.cleaned_data['type_of_leave'] == 'station' \
            and self.cleaned_data['leave_address'] == '':

            raise ValidationError('If on Station Leave, specify Leave Address')
        return self.cleaned_data['leave_address']
