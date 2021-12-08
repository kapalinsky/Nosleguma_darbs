from .models import StudentModel
from django import forms


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = (
            'name',
            'grades',
        )
