# Generated by Django 3.2.8 on 2022-04-17 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=200, verbose_name='رنگ')),
                ('size', models.CharField(max_length=200, verbose_name='اندازه')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.productcategory', verbose_name='دسته بندی'),
        ),
        migrations.AddField(
            model_name='product',
            name='productinformation',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_information', to='product.productinformation', verbose_name='اطلاعات تکمیلی'),
        ),
    ]
