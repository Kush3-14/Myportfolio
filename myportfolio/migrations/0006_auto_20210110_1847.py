# Generated by Django 3.1.3 on 2021-01-10 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_connection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='responsibilities',
        ),
        migrations.AddField(
            model_name='experience',
            name='company',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='location',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibilities_1',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibilities_2',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibilities_3',
            field=models.CharField(default=None, max_length=2000),
        ),
        migrations.AddField(
            model_name='experience',
            name='responsibilities_4',
            field=models.CharField(default=None, max_length=2000),
        ),
    ]
