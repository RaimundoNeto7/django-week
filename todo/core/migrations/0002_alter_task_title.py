# Generated by Django 3.2 on 2021-05-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(help_text='title', max_length=128),
        ),
    ]
