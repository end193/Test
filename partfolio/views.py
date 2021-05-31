from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from .models import PortfolioModel


class PortfolioListView(ListView):
    """ Portfolio ListView """
    
    template_name = "partfolio/partfolio.html"
    model = PortfolioModel
    context_object_name = 'portfolio'
    paginate_by = 5 