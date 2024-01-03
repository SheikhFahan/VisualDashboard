# Generated by Django 4.2.4 on 2024-01-03 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_coffermodel_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffermodel',
            name='added',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='insight',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='intensity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='likelihood',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='pestle',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='published',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='relevance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='sector',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='topic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='coffermodel',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
