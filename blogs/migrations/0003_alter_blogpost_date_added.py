# Generated by Django 3.2.7 on 2021-09-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_blogpost_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]