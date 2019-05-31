from django.db import models
from django.contrib.auth.models import User


class Lesson(models.Model):
    user = models.ForeignKey(User, default=1, related_name='lesson_user', on_delete=models.CASCADE)
    code = models.CharField(max_length=20, verbose_name="Code")
    name = models.CharField(max_length=120, verbose_name="Name")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Lessons"
        verbose_name = "Lesson"
