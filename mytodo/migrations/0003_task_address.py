# Generated by Django 3.2.3 on 2021-06-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytodo', '0002_task_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='address',
            field=models.CharField(default='Jhapa', max_length=100),
        ),
    ]
