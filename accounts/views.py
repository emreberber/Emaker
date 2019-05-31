from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# for image upload with ajax
from django.http import JsonResponse


def login_user(request):
    if request.user.is_authenticated:
        return redirect('lesson:index')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        auth = authenticate(username=username, password=password)
        login(request, auth)
        return redirect('accounts:register')

    return render(request, 'accounts/login.html', context={'form': form})


@login_required(login_url='/accounts/login')
def profile(request):
    # instance=request.user for form input autocomplete
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user)
    context = {'form': form}

    if request.method == 'POST' and form.is_valid():
        user = form.save(commit=False)
        user.first_name = user.first_name.title()
        user.last_name = user.last_name.upper()
        form.save(commit=True)

        message = 'Profile successfully updated'
        messages.success(request, message, extra_tags='text-green')

        return HttpResponseRedirect(reverse('accounts:profile'))

    return render(request, 'accounts/profile.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect('lesson:index')

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')

        user.set_password(password)
        user.save()

        auth = authenticate(username=username, password=password)

        if auth and auth.is_active:
            login(request, auth)
            return redirect('lesson:index')

    return render(request, 'accounts/register.html', context={'form': form})


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('accounts:login'))


def profile_photo(request):
    if request.method == 'POST':
        form = UserProfilePhotoForm(instance=request.user.user_profile, data=request.POST, files=request.FILES)
        if form.is_valid():
            photo = form.save()
            context = {'is_valid': True,'image-url': photo.profile_photo.url}
            return JsonResponse(data=context)
        else:
            return JsonResponse(data={'is_valid': False})
    else:
        return HttpResponseRedirect(reverse('accounts:profile'))




