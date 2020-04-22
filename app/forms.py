from django import forms
from .models import *

class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['full_name', 'faculty', 'speciality', 'group', 'dateOfBirth', 'gender', 'email', 'phone']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'фио'}),
            'dateOfBirth': forms.DateInput(
                attrs={'class': 'input--style-3', 'placeholder': 'дата рождения DD.MM.YYYY'}),
            'phone': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'телефон'}),
            'email': forms.EmailInput(attrs={'class': 'input--style-3', 'placeholder': 'email'}),
            'gender': forms.Select(attrs={'class': 'input--style-3'}),
            'faculty': forms.Select(attrs={'class': 'input--style-3'}),
            'speciality': forms.Select(attrs={'class': 'input--style-3'}),
            'group': forms.Select(attrs={'class': 'input--style-3'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['speciality'].queryset = Specialitys.objects.none()
        self.fields['group'].queryset = Groups.objects.none()

        if 'faculty' in self.data:
            try:
                faculty_id = int(self.data.get('faculty'))
                self.fields['speciality'].queryset = Specialitys.objects.filter(faculty_id=faculty_id).order_by('title')

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['speciality'].queryset = self.instance.faculty.speciality_set.order_by('title')

        if 'speciality' in self.data:
            try:
                speciality_id = int(self.data.get('speciality'))
                self.fields['group'].queryset = Groups.objects.filter(speciality_id=speciality_id).order_by('title')

            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:

            self.fields['group'].queryset = self.instance.speciality.groups_set.order_by('title')