from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import ExamForm, ExamQuestionForm
from .models import Exam
from .models import Question
from django.contrib.auth.decorators import login_required
from . import isowner


# /exam
@login_required(login_url='/accounts/login')
def index(request):
    exams = Exam.objects.filter(user=request.user)
    return render(request, 'exam/index.html', context={'exams': exams})


# /exam/create/?lesson_id=4
@login_required(login_url='/accounts/login')
def create(request):
    if not request.GET.get('lesson_id'):
        message = 'Please, firstly select a lesson'
        messages.success(request, message, extra_tags='text-red x')
        return HttpResponseRedirect(reverse('lesson:index'))

    form = ExamForm(request.POST or None)
    form.fields['questions'].queryset = Question.objects.filter(user_id=request.user, lesson_id=request.GET.get('lesson_id'))
    questions = Question.objects.filter(user=request.user, lesson_id=request.GET.get('lesson_id'))

    context = {'form': form, 'questions': questions}

    if form.is_valid():
        exam = form.save(commit=False)
        exam.user = request.user
        exam.save()
        form.save_m2m()

        message = exam.title + ' successfull created'
        messages.success(request, message, extra_tags='text-green')

        return HttpResponseRedirect(reverse('exam:index'))

    return render(request, 'exam/create.html', context)


# /exam/update/20?lesson_id=4
def update(request, id):
    exam = get_object_or_404(Exam, id=id)

    # exam belongs to the user ?
    if not isowner(exam, request.user):
        return HttpResponseRedirect(reverse('exam:index'))

    form = ExamForm(request.POST or None, request.FILES or None, instance=exam)
    form.fields['questions'].queryset = Question.objects.filter(user_id=request.user,lesson_id=request.GET.get('lesson_id'))
    questions = Question.objects.filter(user=request.user, lesson_id=request.GET.get('lesson_id'))

    context = {'form': form, 'id': id, 'questions': questions}

    if form.is_valid():
        exam.title = exam.title.title()
        form.save()
        message = exam.title + ' successfully updated'
        messages.success(request, message, extra_tags='text-green')

        return redirect('/exam?lesson_id=' + str(exam.lesson_id))

    return render(request, 'exam/update.html', context)


# /exam/delete/20
def delete(request, id):
    exam = get_object_or_404(Exam, id=id)
    exam.delete()

    message = exam.title + ' successfully deleted'
    messages.error(request, message, extra_tags='text-red')

    return redirect('/exam')


# exam/20
def exam(request, id):
    exam = Exam.objects.filter(id=id)
    question = Question.objects.filter(questions__in=exam)

    if request.GET.get('random') == 'True':
        question = Question.objects.filter(questions__in=exam).order_by('?')

    # get half of array in templates
    qnum = question.count()
    qnum_med = qnum//2

    exam = get_object_or_404(Exam, id=id)
    lesson_id = exam.lesson_id

    context = {'question': question, 'exam': exam, 'id': id, 'qnum': qnum, 'qnum_med': qnum_med, 'lesson_id': lesson_id}
    return render(request, 'exam/exam.html', context)


