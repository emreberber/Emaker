from django.db import models
from django.contrib.auth.models import User
from lesson.models import Lesson
from question.models import Question
from ckeditor.fields import RichTextField


class Exam(models.Model):
    user = models.ForeignKey(User, related_name='exam_user', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, related_name='exam_lesson', null=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=120, null=True, verbose_name="Title")
    metadata = RichTextField(max_length=480, null=True, verbose_name="Metadata")

    questions = models.ManyToManyField(Question, related_name='questions')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.metadata

    class Meta:
        verbose_name_plural = "Exams"
        verbose_name = "Exam"






