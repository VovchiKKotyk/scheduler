# Generated by Django 5.1.2 on 2024-11-01 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='order',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
    ]
