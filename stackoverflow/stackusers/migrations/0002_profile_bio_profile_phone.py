# Generated by Django 5.1.2 on 2024-10-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stackusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
