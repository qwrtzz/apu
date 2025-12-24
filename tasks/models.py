from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    # Choices для статуса
    STATUS_CHOICES = [
        ('pending', 'Ожидает выполнения'),
        ('in_progress', 'В процессе'),
        ('done', 'Выполнена'),
    ]
    
    # Choices для приоритета
    PRIORITY_CHOICES = [
        ('low', 'Низкий'),
        ('medium', 'Средний'),
        ('high', 'Высокий'),
    ]
    
    # Поля модели
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(blank=True, verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Статус'
    )
    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name='Приоритет'
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Срок выполнения'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создана')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлена')
    
    class Meta:
        ordering = ['-created_at']  # Сортировка по умолчанию
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
    
    def __str__(self):
        return self.title