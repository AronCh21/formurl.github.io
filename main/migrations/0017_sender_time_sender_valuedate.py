# Generated by Django 4.1.7 on 2023-04-01 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_sender'),
    ]

    operations = [
        migrations.AddField(
            model_name='sender',
            name='time',
            field=models.CharField(default='11:30:31', max_length=500),
        ),
        migrations.AddField(
            model_name='sender',
            name='valueDate',
            field=models.CharField(default='04/01/23', max_length=500),
        ),
    ]
