# Generated by Django 4.2.5 on 2024-05-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(default='a', max_length=2),
        ),
    ]
