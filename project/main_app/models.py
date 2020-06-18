from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='images/news/', verbose_name='Изображение')
    video = models.FileField(upload_to='videos/news/', verbose_name='Видео', blank=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={"pk": self.pk})


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Название категории', null=True)
    image = models.ImageField(upload_to='images/category/', verbose_name='Изображение', null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('news')


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    image = models.ImageField(upload_to='images/products/', verbose_name='Изображение товара')
    sub_category = models.ForeignKey('Category', verbose_name='Подкатегория товара', on_delete=models.CASCADE,
                                     related_name='subcategory')
    options = models.TextField(verbose_name='Характериситики товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={
            'pk': self.pk
        })


class Manager(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя')
    image = models.ImageField(upload_to='images/managers/', verbose_name='Фото')
    chat_id = models.IntegerField(verbose_name='Чат id telegram', null=True)

    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return self.name
