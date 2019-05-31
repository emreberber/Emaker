from django.db import models
from django.contrib.auth.models import User
from lesson.models import Lesson
from ckeditor.fields import RichTextField

LEVEL = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]
ANSWER_TEST = [('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')]
ANSWER_BOOLEAN = [('TRUE', 'TRUE'), ('FALSE', 'FALSE')]


class Question(models.Model):
    user = models.ForeignKey(User, related_name='question_user', on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, null=True, blank=True, related_name='question_lesson', on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True, blank=True, verbose_name="Title")
    subject = models.CharField(max_length=120, null=True, blank=True, verbose_name="Subject")
    level = models.IntegerField(choices=LEVEL, null=True, blank=True, verbose_name="Level")
    style = models.CharField(max_length=10, verbose_name="Style")

    question = RichTextField(max_length=480, null=True, blank=True, verbose_name="Question")
    answer = models.CharField(max_length=480, verbose_name="Answer")
    line = models.IntegerField( verbose_name="Number of Lines", default=0)

    answer_a = models.CharField(max_length=240, verbose_name="A")
    answer_b = models.CharField(max_length=240, verbose_name="B")
    answer_c = models.CharField(max_length=240, verbose_name="C")
    answer_d = models.CharField(max_length=240, verbose_name="D")

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Questions"
        verbose_name = "Question"

