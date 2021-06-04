from django.shortcuts import render
from django.views.generic import ListView
from .models import News


class NewsListView(ListView):
    """ News ListView """
    
    template_name = "news/news.html"
    model = News
    context_object_name = 'news'
    paginate_by = 5 