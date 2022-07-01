from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Todo(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    description = models.TextField(verbose_name='Описание')
    STATUS_CHOICES = (
        ('PLANNED', 'Запланированно'),
        ('PROCESS', 'В процессе'),
        ('DONE', 'Завершено'),
    )
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, default='PLANNED', max_length=50)
    category = models.ManyToManyField(Category, verbose_name='Категория', related_name='todo')
    deadline = models.DateTimeField(verbose_name='Дедлайн', auto_now=False, auto_now_add=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'