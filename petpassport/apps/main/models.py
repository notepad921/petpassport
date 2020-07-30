from django.db import models


class Record(models.Model):
    title = models.CharField('Заголовок', max_length = 50)
    record = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
