# Generated by Django 3.2.8 on 2022-04-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='is_read_by_admin',
            field=models.BooleanField(default=False, verbose_name='خوانده شده توسط ادمین'),
        ),
    ]
