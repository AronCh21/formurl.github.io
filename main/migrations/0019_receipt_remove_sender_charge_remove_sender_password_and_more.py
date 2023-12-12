# Generated by Django 4.1.7 on 2023-04-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_sender_charge_alter_sender_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=10000)),
                ('sender', models.CharField(max_length=10000)),
                ('time', models.CharField(default='12:37:50', max_length=500)),
                ('valueDate', models.CharField(default='04/02/23', max_length=500)),
                ('payoutAmtUsd', models.CharField(max_length=500)),
                ('rate', models.CharField(max_length=500)),
                ('charge', models.CharField(blank=True, max_length=500)),
                ('password', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='sender',
            name='charge',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='password',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='payoutAmtUsd',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='rate',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='time',
        ),
        migrations.RemoveField(
            model_name='sender',
            name='valueDate',
        ),
    ]
