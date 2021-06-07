from landing.models import ServicesModel
from .models import Order
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegisterUserForm, OrderForm



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


class AccountView(LoginRequiredMixin, TemplateView):
    """ Аккаунт """

    template_name = 'users/account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_list'] = Order.objects.filter(client=self.request.user)
        
        return context


class OrderCreateView(LoginRequiredMixin, CreateView):
    """ Создание заказа """

    model = ServicesModel
    template_name = 'users/modify_order.html'
    form_class = OrderForm
    # fields = ['service', 'description', 'phone_number']
    success_url = reverse_lazy('users:account')

    def get_context_data(self):
        context = super().get_context_data()
        context['name'] = 'Заказ услуги'
        return context

    def form_valid(self, form):
        form.instance.client = self.request.user
        return super().form_valid(form)


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    """Удалить заказ"""

    model = Order
    success_url = reverse_lazy('users:account')

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(client=self.request.user)
    
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)