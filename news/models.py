from django.db import models
 
class News(models.Model):
    """Новости сайта"""
    
    title = models.CharField('Заголовок', max_length=150)
    content = models.TextField('Текст', max_length=10000)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
   
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-date']
        verbose_name = ('Новости')
        verbose_name_plural = ('Новости')