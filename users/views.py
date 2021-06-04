from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterUserForm



class UserLoginView(LoginView):
    """ Вход пользователя """

    template_name = 'users/login.html'


class RegisterUserView(CreateView):
    """ Регистрация пользователя """

    model = User
    template_name = 'users/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('users:account')


class UserLogoutView(LogoutView):
    """ Выход """


class AccountView(TemplateView):
    """ Аккаунт """

    template_name = 'users/account.html'