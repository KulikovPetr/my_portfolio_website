from django.db import models


class Article(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Содержимое')
    video_text = models.TextField('Вставка_видео', default="")

    def get_absolute_url(self):
        return f'/projects/{self.id}'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

