from django.db import models


class Articles(models.Model):
    title = models.CharField(max_length= 120, verbose_name='Заголовок')
    post = models.TextField(verbose_name= 'Текст')
    author = models.CharField(max_length= 30, verbose_name='Автор')
    data = models.DateTimeField(verbose_name='Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

