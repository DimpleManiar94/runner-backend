# Generated by Django 2.1.5 on 2019-02-25 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskTitle', models.CharField(max_length=200)),
                ('Description', models.TextField()),
                ('Reward', models.IntegerField()),
                ('DateOfCompletion', models.DateField()),
                ('TimeOfCompletion', models.TimeField()),
                ('Addr1', models.CharField(max_length=200)),
                ('Addr2', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('PostalCode', models.CharField(max_length=10)),
                ('TaskType', models.CharField(choices=[('Shopping', 'Shopping'), ('Moving', 'Moving'), ('Lifting', 'Lifting')], max_length=10)),
                ('TaskStatus', models.CharField(choices=[('Available', 'Available'), ('Running', 'Running'), ('Completed', 'Completed')], max_length=10)),
                ('CreatedTS', models.DateTimeField(auto_now_add=True)),
                ('UpdatedTS', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
