# Generated by Django 4.0.6 on 2023-03-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('byOrder', models.CharField(max_length=500)),
                ('tel', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('country', models.CharField(max_length=500)),
                ('nationality', models.CharField(max_length=500)),
            ],
        ),
    ]