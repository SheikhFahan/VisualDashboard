# Generated by Django 4.2.4 on 2024-01-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_coffermodel_country_alter_coffermodel_impact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffermodel',
            name='url',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]