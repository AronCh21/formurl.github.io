# Generated by Django 4.0.6 on 2023-03-18 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_createpdf_time_alter_createpdf_valuedate'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Beneficiary',
        ),
        migrations.DeleteModel(
            name='Sender',
        ),
        migrations.AlterField(
            model_name='createpdf',
            name='time',
            field=models.TimeField(blank=True, default='14:42:22'),
        ),
        migrations.AlterField(
            model_name='createpdf',
            name='valueDate',
            field=models.CharField(blank=True, default='03/18/23', max_length=50),
        ),
    ]
