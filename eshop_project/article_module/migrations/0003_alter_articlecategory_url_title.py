# Generated by Django 4.0.4 on 2022-04-25 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_module', '0002_alter_articlecategory_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='url_title',
            field=models.CharField(max_length=200, unique=True, verbose_name='عنوان در url'),
        ),
    ]
