# Generated by Django 2.2.10 on 2020-03-29 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slack', '0010_auto_20200309_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreate',
            name='text',
            field=models.TextField(max_length=255),
        ),
    ]
