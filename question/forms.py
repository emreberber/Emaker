from django import forms
from .models import Question, Lesson, LEVEL, ANSWER_TEST, ANSWER_BOOLEAN
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField


class TestQuestionForm(forms.ModelForm):
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'lesson',
        'autocomplete': 'off'
        }))

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'title',
        'autocomplete': 'off'
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'autocomplete': 'off'
    }))
    
    question = forms.CharField(widget=CKEditorWidget())

    level = forms.CharField(widget=forms.Select(choices=LEVEL, attrs={
        'class': 'form-control',
        'id': 'level',
        'autocomplete': 'off',
    }))

    answer_a = forms.CharField(widget=CKEditorWidget())

    answer_b = forms.CharField(widget=CKEditorWidget())

    answer_c = forms.CharField(widget=CKEditorWidget())

    answer_d = forms.CharField(widget=CKEditorWidget())

    answer = forms.CharField(widget=forms.Select(choices=ANSWER_TEST, attrs={
        'class': 'form-control',
        'id': 'answer',
        'autocomplete': 'off',
    }))

    class Meta:
        model = Question
        fields = [
            'lesson',
            'title',
            'subject',
            'level',
            'question',
            'answer_a',
            'answer_b',
            'answer_c',
            'answer_d',
            'answer'
        ]


class ClassicQuestionForm(forms.ModelForm):
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'lesson',
        'autocomplete': 'off'
    }))

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'title',
        'autocomplete': 'off'
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'autocomplete': 'off'
    }))

    question = forms.CharField(widget=CKEditorWidget())

    level = forms.CharField(widget=forms.Select(choices=LEVEL, attrs={
        'class': 'form-control',
        'id': 'level',
        'autocomplete': 'off',
    }))

    line = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'line',
        'autocomplete': 'off'
    }))

    answer = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Question
        fields = [
            'lesson',
            'title',
            'subject',
            'level',
            'line',
            'question',
            'answer'
        ]


class BooleanQuestionForm(forms.ModelForm):
    lesson = forms.ModelChoiceField(queryset=Lesson.objects.all(), widget=forms.Select(attrs={
        'class': 'form-control',
        'id': 'lesson',
        'autocomplete': 'off'
    }))

    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'title',
        'autocomplete': 'off'
    }))

    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'subject',
        'autocomplete': 'off'
    }))

    question = forms.CharField(widget=CKEditorWidget())

    level = forms.CharField(widget=forms.Select(choices=LEVEL, attrs={
        'class': 'form-control',
        'id': 'level',
        'autocomplete': 'off',
    }))

    answer = forms.CharField(widget=forms.Select(choices=ANSWER_BOOLEAN, attrs={
        'class': 'form-control',
        'id': 'answer',
        'autocomplete': 'off',
    }))

    class Meta:
        model = Question
        fields = [
            'lesson',
            'title',
            'subject',
            'level',
            'question',
            'answer'
        ]
