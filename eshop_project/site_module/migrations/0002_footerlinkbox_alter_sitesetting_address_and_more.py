# Generated by Django 4.0.4 on 2022-04-25 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک های فوتر',
                'verbose_name_plural': 'دسته بندی های لینک های فوتر',
            },
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='address',
            field=models.CharField(max_length=255, verbose_name='ادرس '),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='copy_right',
            field=models.CharField(max_length=255, verbose_name='متن کپی رایت ,سایت'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='fax',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='فاکس '),
        ),
        migrations.AlterField(
            model_name='sitesetting',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='تلفن '),
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='عنوان')),
                ('url', models.URLField(max_length=250, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': '  لینک  فوتر',
                'verbose_name_plural': '   لینک های فوتر',
            },
        ),
    ]
