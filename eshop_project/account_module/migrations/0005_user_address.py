# Generated by Django 4.0.4 on 2022-04-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0004_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='ادرس'),
        ),
    ]