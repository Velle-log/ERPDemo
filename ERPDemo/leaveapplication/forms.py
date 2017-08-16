from django import forms
from .models import Leave
from datetime import datetime
from .models import RemainingLeaves

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
            'purpose': forms.Textarea,
        }


    def clean(self):

        replacing_user = self.cleaned_data['replacing_user']
        if replacing_user == self.user:
            raise forms.ValidationError('Can\'t choose yourself as replacing user')

        try:
            start_date = self.cleaned_data['start_date']
            end_date = self.cleaned_data['end_date']
            type_of_leave = self.cleaned_data['type_of_leave']

        except KeyError:
            raise forms.ValidationError('Invalid Input, Check whether dates are valid or not.')

        if start_date > end_date or start_date.strftime("%m/%d/%Y") < datetime.now().strftime("%m/%d/%Y"):
            raise forms.ValidationError('Invalid Dates Entered')

        leave_days = (self.cleaned_data['end_date'] - self.cleaned_data['start_date']).days + 1

        if type_of_leave == 'station':
            if self.cleaned_data['leave_address'] == '':
                raise forms.ValidationError('If on Station Leave, specify Leave Address')

            elif leave_days > 2:
                raise forms.ValidationError('Maximum 2 Station Leaves at a time allowed')

            elif start_date.weekday() not in [5, 6] or end_date.weekday() not in [5, 6]:
                raise forms.ValidationError('Only Weekends can be taken as Station Leaves')

        elif type_of_leave == 'vacation':

            if not (start_date.strftime("%m/%d") > "05/05" and end_date.strftime("%m/%d") < "07/25"):
                raise forms.ValidationError("Vacation Leaves can be taken only in vacation period, (05-May to 25-July)")

        user_leave_data = RemainingLeaves.objects.get(user=self.user)
        remaining_leaves = getattr(user_leave_data, type_of_leave, 2)
        print(leave_days, remaining_leaves)
        if leave_days > remaining_leaves:
            raise forms.ValidationError('Only {} {} leaves remaining'.format(remaining_leaves, self.cleaned_data['type_of_leave']))

        return self.cleaned_data


class StudentLeave(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(StudentLeave, self).__init__(*args, **kwargs)
        for field in self.fields:
            if 'date' not in field:
                self.fields[field].widget.attrs['class'] = 'form-control'

    class Meta:

        model = Leave
        fields = ['start_date', 'end_date', 'purpose', 'leave_address']
        widgets = {
            'start_date': forms.SelectDateWidget(),
            'end_date': forms.SelectDateWidget(),
            'purpose': forms.Textarea,
        }

    def clean(self):
        try:
            start_date = self.cleaned_data['start_date']
            end_date = self.cleaned_data['end_date']

        except KeyError:
            raise forms.ValidationError('Invalid Input, Check whether dates are valid or not.')

        if start_date > end_date or start_date.strftime("%m/%d/%Y") < datetime.now().strftime("%m/%d/%Y"):
            raise forms.ValidationError('Invalid Dates Entered')
