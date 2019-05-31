from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from lesson.models import *
from question.models import *
from .forms import LessonForm
from . import isowner


# /lesson
@login_required(login_url='/accounts/login')
def index(request):
    lessons = Lesson.objects.filter(user=request.user)
    return render(request, 'lesson/index.html', context={'lessons': lessons})


# /lesson/create
@login_required(login_url='/accounts/login')
def create(request):
    form = LessonForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        lesson = form.save(commit=False)
        lesson.user = request.user
        lesson.code = lesson.code.upper()
        lesson.name = lesson.name.title()
        lesson.save()

        message = lesson.code + ' - ' + lesson.name + ' successfully created'
        messages.success(request, message, extra_tags='text-green')

        return HttpResponseRedirect(reverse('lesson:index'))

    return render(request, 'lesson/create.html', context)


# /lesson/update/{id}
@login_required(login_url='/accounts/login')
def update(request, id):
    lesson = get_object_or_404(Lesson, id=id)

    if not isowner(lesson, request.user):
        return HttpResponseRedirect(reverse('lesson:index'))

    form = LessonForm(data=request.POST or None, instance=lesson)
    context = {'form': form, 'id': id}

    if request.method == 'POST' and form.is_valid():
        lesson.code = lesson.code.upper()
        lesson.name = lesson.name.title()
        form.save()

        message = lesson.code + ' - ' + lesson.name + ' successfully updated'
        messages.success(request, message, extra_tags='text-green')

        return HttpResponseRedirect(reverse('lesson:index'))

    return render(request, 'lesson/update.html', context)


# /lesson/delete/{id}
@login_required(login_url='/accounts/login')
def delete(request, id):
    lesson = get_object_or_404(Lesson, id=id)
    lesson.delete()

    message = lesson.code + ' - ' + lesson.name + ' successfully deleted'
    messages.success(request, message, extra_tags='text-red')

    return HttpResponseRedirect(reverse('lesson:index'))

