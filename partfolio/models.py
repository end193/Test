from django.db import models


class PortfolioModel(models.Model):
    """ Модель для Портфолио """

    title = models.CharField('Название проекта', max_length=30)
    description = models.CharField('Описание проекта', max_length=300)
    image = models.ImageField(upload_to='portfolio/')
    url_address = models.URLField(max_length=200)
    date = models.DateTimeField('Дата создания')

    def str(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name = ('Портфолио')
        verbose_name_plural = ('Портфолио')
    
    # Вывод изображений в админке
    def get_image(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(
                u'<a href="{0}" target="_blank"><img src="{0}" width="100" heigth="100" style="border-radius: 10%; border: 2px solid #ccc;"/></a>'.format(self.image.url)
            )
        else:
            return '(Нет изображения)'

    get_image.short_description = 'Изображение'
    get_image.allow_tags = True        