# Generated by Django 4.2.4 on 2023-12-29 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_rename_economicindicator_coffermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffermodel',
            name='end_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='start_year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
