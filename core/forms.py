from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category', 'name', 'description', 'price', 'image')
        widgets = {
                'category': forms.Select(attrs={
                        'class': INPUT_CLASSES
                    }),
                'name': forms.TextInput(attrs={
                        'class': INPUT_CLASSES
                    }),
                'description': forms.Textarea(attrs={
                        'class': INPUT_CLASSES
                    }),
                'price': forms.TextInput(attrs={
                        'class': INPUT_CLASSES
                    }),
                'image': forms.FileInput(attrs={
                        'class': INPUT_CLASSES
                    }),
            }

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    password = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your password',
            'class': 'w-full py-4 px-6 rounded-xl'
        }))
    

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Your email',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'your password',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': 'confirm password',
            'class': 'w-full py-4 px-6 rounded-xl',
        }))
    
