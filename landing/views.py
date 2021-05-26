from django.shortcuts import render
from django.views.generic.base import TemplateView
from news.models import News # Импорт модели из другого приложение

class LandingView(TemplateView):
    """ Landing View """
    
    template_name = "landing/landing.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['news'] = News.objects.all()[:5] # забираем последние 5 новостей
        return context