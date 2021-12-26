from django.contrib import admin
from django.urls import path, include
from . import views
from user.views import editar_user

app_name = "user"

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('editar/', editar_user, name='Editar'),
    path('dashboard/', views.dashboard, name="dashboard"),
]
