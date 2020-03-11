# Generated by Django 2.2.10 on 2020-02-26 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0005_auto_20200226_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pasword',
        ),
        migrations.RemoveField(
            model_name='user',
            name='repasword',
        ),
        migrations.AddField(
            model_name='user',
            name='password1',
            field=models.CharField(default='パスワード', max_length=2000),
        ),
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default='再入力パスワード', max_length=2000),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='名前', max_length=255),
        ),
    ]
