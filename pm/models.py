# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cource(models.Model):
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
    title = models.CharField(verbose_name='Название', max_length=256)
    short_title = models.CharField(verbose_name='Аббревиатура', max_length=32)
    schedule = models.URLField(verbose_name='Расписание')
    bg_color = models.CharField(verbose_name='Цвет фона', max_length=8,
                                default="FFE4B5")
    title_color = models.CharField(verbose_name='Цвет заколовка', max_length=8,
                                   default="8B2500")
    lecturer = models.TextField(verbose_name='Лектор')

    def __unicode__(self):
        return self.short_title

class CourceItem(models.Model):
    class Meta:
        abstract = True
    cource = models.ForeignKey(Cource)

class News(CourceItem):
    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    pub_date = models.DateTimeField(verbose_name='Дата публикации',
                                    auto_now_add=True)
    author = models.ForeignKey(User, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')

    def __unicode__(self):
        return self.title

class Link(CourceItem):
    class Meta:
        verbose_name = 'Ресурс'
        verbose_name_plural = 'Ресурсы'
    name = models.CharField(verbose_name='Название', max_length=128)
    href = models.URLField(verbose_name='Ссылка')
    title = models.CharField(verbose_name='Описание', max_length=256,
                             blank=True)

    def __unicode__(self):
        return self.name

class Handout(CourceItem):
    class Meta:
        verbose_name = 'Раздаточный материал'
        verbose_name_plural = 'Раздаточные материалы'
    name = models.CharField(verbose_name='Название', max_length=256)
    file = models.FileField(verbose_name='Файл', upload_to='handouts/')

    def __unicode__(self):
        return self.name

class Assignment(CourceItem):
    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
    name = models.CharField(verbose_name='Название', max_length=256)
    file = models.FileField(verbose_name='Файл', upload_to='assignments/')

    def __unicode__(self):
        return self.name

class Progress(CourceItem):
    class Meta:
        get_latest_by = 'year'
        verbose_name = 'Список успеваемости'
        verbose_name = 'Списки успеваемости'
    year = models.IntegerField(verbose_name='Год')
    doc = models.URLField(verbose_name='Ссылка')


