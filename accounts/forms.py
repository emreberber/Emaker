from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'autocomplete': 'off'
    }))

    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'autocomplete': 'off'
    }))


class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'autocomplete': 'off'
    }))

    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'autocomplete': 'off'
    }))

    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'autocomplete': 'off'
    }))

    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'autocomplete': 'off'
    }))

    password1 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password',
        'autocomplete': 'off'
    }))

    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password Again',
        'autocomplete': 'off'
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2


class UserProfileForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        'autocomplete': 'off'
    }))

    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name',
        'autocomplete': 'off'
    }))

    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name',
        'autocomplete': 'off'
    }))

    email = forms.EmailField(max_length=254, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email',
        'autocomplete': 'off'
    }))

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class UserProfilePhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo', 'user']
