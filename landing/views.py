from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import ServicesModel


class LandingView(TemplateView):
    """ Landing View """
    
    template_name = "landing/landing.html"


class ServicesListView(ListView):
    """ Services ListView """
    
    template_name = "landing/services.html"
    model = ServicesModel
    context_object_name = 'services'
    paginate_by = 5


class ContactView(TemplateView):
    """ Contact View """
    
    template_name = "landing/contact.html"