# Generated by Django 4.1.7 on 2023-03-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_designs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='max_bedrooms',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='plan',
            name='min_bedrooms',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
