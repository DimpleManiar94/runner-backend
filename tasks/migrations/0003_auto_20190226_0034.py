# Generated by Django 2.1.5 on 2019-02-26 00:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20190225_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='RunnerFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='runner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='TaskType',
            field=models.CharField(choices=[('Shopping', 'Shopping'), ('Moving', 'Moving'), ('Lifting', 'Lifting'), ('Other', 'Other')], max_length=10),
        ),
    ]
