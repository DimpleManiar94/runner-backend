# Generated by Django 2.1.5 on 2019-02-26 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='ProfilePicture',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]