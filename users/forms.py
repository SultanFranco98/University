from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(max_length=50,
                                widget=forms.PasswordInput(attrs={'class': 'input--style-3', 'placeholder': 'пароль*'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(
        attrs={'class': 'input--style-3', 'placeholder': 'подвердить пароль*'}))

    class Meta:
        model = Users
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input--style-3', 'placeholder': 'логин*'}),
        }

    def create(self, validated_data):
        return Users.objects.create_user(**validated_data)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'input--style-3', 'placeholder': 'имя пользователя'}))
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'input--style-3', 'placeholder': 'пароль'}))

    class Meta:
        model = Users
        fields = ['username', 'password']
