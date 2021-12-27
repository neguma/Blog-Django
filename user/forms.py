from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import fields
from django.forms.widgets import PasswordInput


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    email = forms.EmailField(label='Correco electrónico')
    username = forms.CharField(max_length=50, label="Usuario ")
    password = forms.CharField(max_length=30, label="Contraseña ", widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=30, label="Confirmar contraseña", widget=forms.PasswordInput)


    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and (password != confirm):
            raise forms.ValidationError("Las contraseñas no coinciden")

        values = {
            "username": username,
            "password": password,
        }
        return values


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario ")
    password = forms.CharField(label="Contraseña", widget=PasswordInput)


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Editar Email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repetir contraseña', widget=forms.PasswordInput)

    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}
