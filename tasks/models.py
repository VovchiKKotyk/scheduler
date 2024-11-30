
from django.db import models

class Task(models.Model):
    title = models.CharField("Назва завдання", max_length=200)
    description = models.TextField("Опис", blank=True, null=True)
    date = models.DateField("Дата виконання")
    time = models.TimeField("Час виконання", blank=True, null=True)
    status = models.CharField("Статус", max_length=20, choices=[('pending', 'Не виконано'), ('completed', 'Виконано')], default='pending')
    order = models.PositiveIntegerField("Порядок", default=0)  # Поле для зберігання порядку
    PRIORITY_CHOICES = [
        ('low', 'Низький'),
        ('medium', 'Середній'),
        ('high', 'Високий'),
    ]
    priority = models.CharField("Пріоритет", max_length=10, choices=PRIORITY_CHOICES, default='medium')
    CATEGORY_CHOICES = [
        ('work', 'Робота'),
        ('personal', 'Особисте'),
        ('study', 'Навчання'),
        ('other', 'Інше'),
    ]
    category = models.CharField("Категорія", max_length=10, choices=CATEGORY_CHOICES, default='other')


    def __str__(self):
        return self.title
