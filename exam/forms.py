from django import forms
from .models import Exam, Lesson, Question
from ckeditor.widgets import CKEditorWidget


class ExamForm(forms.ModelForm):
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

	metadata = forms.CharField(widget=CKEditorWidget())

	questions = forms.ModelMultipleChoiceField(
		widget=forms.CheckboxSelectMultiple,
		required=True,
		queryset=Question.objects.all()
	)

	class Meta:
		model = Exam
		fields = [
			'lesson',
			'title',
			'metadata',
			'questions'
		]


# ?
class ExamQuestionForm(forms.ModelForm):

	class Meta:
		model = Exam
		fields = [
			'questions'
		]
