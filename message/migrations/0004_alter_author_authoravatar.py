# Generated by Django 3.2.5 on 2021-10-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_author_authoruser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='authorAvatar',
            field=models.ImageField(blank=True, upload_to='static/imagination'),
        ),
    ]