# Generated by Django 4.2.5 on 2024-05-24 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_rename_name_category_category_category_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='movie',
            name='rdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
