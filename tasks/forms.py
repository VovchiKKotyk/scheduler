from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'date', 'time', 'status', 'priority', 'category']
        labels = {
            'title': 'Назва завдання',
            'description': 'Опис',
            'date': 'Дата виконання',
            'time': 'Час виконання',
            'status': 'Статус',
            'priority': 'Пріоритет',
            'category': 'Категорія',
        }
        widgets = {
            'date': forms.DateInput(attrs={'type': 'text'}),
            'time': forms.TimeInput(attrs={'type': 'text'}),
        }
