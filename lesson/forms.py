from django import forms
from .models import Lesson


class LessonForm(forms.ModelForm):
    code = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'code',
        'autocomplete': 'off'
    }))

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'name',
        'autocomplete': 'off'
    }))

    class Meta:
        model = Lesson
        fields = [
            'code',
            'name',
        ]
