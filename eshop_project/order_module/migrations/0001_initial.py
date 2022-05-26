# Generated by Django 4.0.4 on 2022-05-07 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0006_productgallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(verbose_name='نهایی شده / نشده')),
                ('payment_data', models.DateField(blank=True, null=True, verbose_name='تاریخ پرداخت')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کابر')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبدهای خرید کاربران ',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_price', models.IntegerField(blank=True, null=True, verbose_name='قیمت نهایی تکی محصول')),
                ('count', models.IntegerField(verbose_name='تعداد')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order_module.order', verbose_name='سبد خرید')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جزئیات سبد خرید',
                'verbose_name_plural': 'لیست جزئیات سبد خرید',
            },
        ),
    ]