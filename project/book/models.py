from django.db import models

# Create your models here.

from django.urls import reverse

class Person(models.Model):
    name = models.CharField('Имя', max_length=100)
    sname = models.CharField('Фамилия', max_length=100)
    country = models.CharField('Страна', max_length=100, blank=True, null=True)
    city = models.CharField('Город', max_length=100, blank=True, null=True)
    street = models.CharField('Улица', max_length=100, blank=True, null=True)
    url = models.URLField('Сылка', blank=True, null=True)
    phone = models.CharField('Телефон', max_length=100)
    photo = models.ImageField('Фото', upload_to='photo/', blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.sname}'

    def get_absolute_url(self):
        return reverse('book:person_detail',
                       args=(self.id,))