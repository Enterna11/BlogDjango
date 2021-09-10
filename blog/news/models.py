from django.db import models
from django.contrib.auth import get_user_model


class Categories(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', unique=True)

    class Meta:
        db_table = 'Category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название', db_index=True)
    content = models.TextField(verbose_name='Содержание')
    photo = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория',
                                 related_name='category')
    author = models.ForeignKey(get_user_model(),
                               on_delete=models.PROTECT,
                               verbose_name='Автор',
                               related_name='author')

    class Meta:
        db_table = 'News'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

