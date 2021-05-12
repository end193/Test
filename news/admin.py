from django.contrib import admin # импортируем класс admin чтобы вызвать у него метод register
from .models import News # Импортируем из models.py класс News
 
 
class NewsAdmin(admin.ModelAdmin):
    """Новости в админке"""
 
    model = News # Указываем модель которую импортировали
    list_display = ('title', 'content', 'date') # Указываем в кортедже используемые поля которые отображаются в админке
 
 
admin.site.register(News, NewsAdmin) # вызываем метод register передаем в метод модель News и класс NewsAdmin, Регистрируем в админку