# Generated by Django 3.0.5 on 2020-05-01 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borghive', '0005_auto_20200501_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='repositoryuser',
            name='user',
        ),
        migrations.AddField(
            model_name='repositoryuser',
            name='name',
            field=models.CharField(default='t80hprhm', max_length=8, unique=True),
        ),
    ]
