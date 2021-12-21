from django import forms
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    username = forms.CharField(max_length= 50, label="Usuario ")
    password = forms.CharField(max_length=30,label="Contraseña ",widget= forms.PasswordInput)
    confirm = forms.CharField(max_length=30,label="Confirmar contraseña",widget=forms.PasswordInput)

    def clean(self) :
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and (password != confirm) :
            raise forms.ValidationError("Las contraseñas no coinciden")

        values = {
            "username" : username,
            "password" : password,
        }
        return values

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario ")
    password = forms.CharField(label="Contraseña",widget=PasswordInput)


