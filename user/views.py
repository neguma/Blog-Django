from typing import NewType
from django.http import request
from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):

    if request.user.is_authenticated:
        messages.info(request,"No te hagas el listo:)")

        return redirect("index")

    else :
        form = forms.RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            newUser = User(username = username)
            newUser.set_password(password)

            newUser.save()
            login(request,newUser)
            messages.success(request,"Registro exitoso")
            return redirect("index")
        context = {
                "form" : form }
        return render(request,"register.html",context)


def login_user(request):

    if request.user.is_authenticated:
        messages.info(request,"No te hagas el listo:)")

        return redirect("index")
    else :
        form = forms.LoginForm(request.POST or None)

        context = {
            "form" : form}

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username,password = password)

            if user is None :
                messages.info(request,"Usuario o contraseña incorrectos.")
                return render(request,"login.html",context)

            messages.success(request,"Login exitoso.")
            login(request,user)
            return redirect("index")
        return render(request,"login.html",context)


def logout_user(request):
    logout(request)
    messages.success(request,"Logout exitoso")
    return redirect("index")

def dashboard(request):
    return render(request,"general.html")

