from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User



class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username','password')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username ',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password ',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    
class SingupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password' ,'pass2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username ',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Your Email address ',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    pass1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password ',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))
    pass2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Repeat Password ',
        'class' : 'w-full py-4 px-6 rounded-xl',
    }))

