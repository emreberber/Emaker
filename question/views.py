from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
from question.forms import TestQuestionForm, ClassicQuestionForm, BooleanQuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from . import isowner


# /question or /question/?lesson_id=4
@login_required(login_url='/accounts/login')
def index(request):
    # Url contain lesson_id param ?
    query = request.GET.get('lesson_id')

    if query:
        questions = Question.objects.filter(user=request.user, lesson_id=query)
        # for content-description block
        lesson = Lesson.objects.get(id=query)
        context = {'questions': questions, 'lesson': lesson}

        return render(request, 'question/index.html', context)

    questions = Question.objects.filter(user=request.user)
    return render(request, 'question/index.html', context={'questions': questions})


# /question/create/?lesson_id=4&style=TEST
@login_required(login_url='/accounts/login')
def create(request):
    num_of_lesson = Lesson.objects.filter(user_id=request.user).count()

    if not num_of_lesson > 0:
        message = 'Please, firstly create a lesson'
        messages.success(request, message, extra_tags='text-red x')
        return HttpResponseRedirect(reverse('question:index'))

    if request.GET.get('style') == 'TEST':
        form = TestQuestionForm(request.POST or None, request.FILES or None)
        form.fields['lesson'].queryset = Lesson.objects.filter(user_id=request.user)
        context = {'form': form}

        query = request.GET.get('lesson_id')
        if query:
            lesson = Lesson.objects.get(id=query)
            context['lesson'] = lesson

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.title = question.title.title()
            question.subject = question.subject.capitalize()
            question.style = 'TEST'
            question.save()

            message = question.title + ' successfully created'
            messages.success(request, message, extra_tags='text-green')

            if query:
                return redirect('/question?lesson_id=' + str(query))

            return HttpResponseRedirect(reverse('question:index'))

        return render(request, 'question/create.html', context)

    elif request.GET.get('style') == 'CLASSIC':
        form = ClassicQuestionForm(request.POST or None, request.FILES or None)
        form.fields['lesson'].queryset = Lesson.objects.filter(user_id=request.user)
        context = {'form': form}

        query = request.GET.get('lesson_id')
        if query:
            lesson = Lesson.objects.get(id=query)
            context['lesson'] = lesson

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.title = question.title.title()
            question.subject = question.subject.capitalize()
            question.style = 'CLASSIC'
            question.save()

            message = question.title + ' successfully created'
            messages.success(request, message, extra_tags='text-green')

            if query:
                return redirect('/question?lesson_id=' + str(query))

            return HttpResponseRedirect(reverse('question:index'))

        return render(request, 'question/create.html', context)

    elif request.GET.get('style') == 'BOOLEAN':
        form = BooleanQuestionForm(request.POST or None, request.FILES or None)
        form.fields['lesson'].queryset = Lesson.objects.filter(user_id=request.user)
        context = {'form': form}

        query = request.GET.get('lesson_id')
        if query:
            lesson = Lesson.objects.get(id=query)
            context['lesson'] = lesson

        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.title = question.title.title()
            question.subject = question.subject.capitalize()
            question.style = 'BOOLEAN'
            question.save()

            message = question.title + ' successfully created'
            messages.success(request, message, extra_tags='text-green')

            if query:
                return redirect('/question?lesson_id=' + str(query))

            return HttpResponseRedirect(reverse('question:index'))

        return render(request, 'question/create.html', context)

    else:
        return HttpResponseRedirect(reverse('question:index'))


# /question/update/39?style=BOOLEAN
@login_required(login_url='/accounts/login')
def update(request, id):
    question = get_object_or_404(Question, id=id)

    # question belongs to the user ?
    if not isowner(question, request.user):
        return HttpResponseRedirect(reverse('lesson:index'))

    # question/update/?style=TEST
    if question.style == 'TEST':
        form = TestQuestionForm(request.POST or None, request.FILES or None, instance=question)
        form.fields['lesson'].queryset = Lesson.objects.filter(user_id=request.user)

        # id for delete button
        context = {'form': form, 'id': id}

        if form.is_valid():
            question.title = question.title.title()
            question.subject = question.subject.capitalize()
            form.save()
            message = question.title + ' successfully updated'
            messages.success(request, message, extra_tags='text-green')

            return redirect('/question?lesson_id=' + str(question.lesson_id))

        return render(request, 'question/update.html', context)

    # /question/update/?style=CLASSIC
    elif question.style == 'CLASSIC':
        form = ClassicQuestionForm(request.POST or None, request.FILES or None, instance=question)
        form.fields['lesson'].queryset = Lesson.objects.filter(user_id=request.user)
        # id for delete button
        context = {'form': form, 'id': id}

        if form.is_valid():
            question.title = question.title.title()
            question.subject = question.subject.capitalize()
            form.save()
            message = question.title + ' successfully updated'
            messages.success(request, message, extra_tags='text-green')

            return redirect('/question?lesson_id=' + str(question.lesson_id))

        return render(request, 'question/update.html', context)

    # /question/update/?style=BOOLEAN
    elif question.style == 'BOOLEAN':
        form = BooleanQuestionForm(request.POST or None, request.FILES or None, instance=question)
        form.fields['lesson'].queryset = Lesson.objects.filter(user_id=request.user)

        # id for delete button
        context = {'form': form, 'id': id}

        if form.is_valid():
            question.title = question.title.title()
            question.subject = question.subject.capitalize()
            form.save()
            message = question.title + ' successfully updated'
            messages.success(request, message, extra_tags='text-green')

            return redirect('/question?lesson_id=' + str(question.lesson_id))

        return render(request, 'question/update.html', context)

    else:
        return HttpResponseRedirect(reverse('question:index'))


# /question/delete/39
@login_required(login_url='/accounts/login')
def delete(request, id):
    question = get_object_or_404(Question, id=id)
    question.delete()

    message = question.title + ' successfully deleted'
    messages.error(request, message, extra_tags='text-red')

    return redirect('/question?lesson_id=' + str(question.lesson_id))
