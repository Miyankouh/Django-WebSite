# Generated by Django 4.0.4 on 2022-04-25 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0004_slider_is_active_alter_slider_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.URLField(max_length=500, verbose_name='ادرس'),
        ),
    ]
