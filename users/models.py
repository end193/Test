from django.db import models
from landing.models import ServicesModel
from django.contrib.auth.models import User
from django.urls import reverse


class StatusOrder(models.Model):
    """ Статус """

    title = models.CharField('Название', max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = ('Статус')
        verbose_name_plural = ('Статус')


class Order(models.Model):
    """ Заказ услуги """

    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Заказчик')
    service = models.ForeignKey(ServicesModel, on_delete=models.CASCADE, verbose_name='Услуга')
    description = models.TextField('Текст', max_length=10000)
    phone_number = models.CharField('Телефон', max_length=12)
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    status = models.ForeignKey(StatusOrder, on_delete=models.CASCADE, verbose_name='Статус заказа', default=1)

    def __str__(self):
        return self.service.title

    class Meta:
        ordering = ['-date']
        verbose_name = ('Заказ пользователя')
        verbose_name_plural = ('Заказы пользователей')


