# Generated by Django 4.1.7 on 2023-03-17 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_designs', '0003_alter_plan_heated_sq_feet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorpicture',
            name='image',
            field=models.ImageField(upload_to='pictures/floor_pictures'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='heated_sq_feet',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='planpicture',
            name='image',
            field=models.ImageField(upload_to='pictures/plan_pictures'),
        ),
    ]
