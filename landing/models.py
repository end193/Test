from django.db import models


class ServicesModel(models.Model):
    """ Модель для Услуги """

    title = models.CharField('Наименование услуги', max_length=30)
    description = models.CharField('Описание услуги', max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Услуги')
        verbose_name_plural = ('Услуги')