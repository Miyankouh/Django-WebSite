from django.db import models
from account_module.models import User
from product.models import Product
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کابر')
    is_paid = models.BooleanField(verbose_name='نهایی شده / نشده')
    payment_data = models.DateField(null=True, blank=True, verbose_name='تاریخ پرداخت')

    def __str__(self):
        return self(self.user)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید کاربران '


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,  verbose_name='محصول')
    final_price = models.IntegerField(null=True, blank=True, verbose_name='قیمت نهایی تکی محصول')
    count = models.IntegerField(verbose_name='تعداد')

    def __str__(self):
        return str(self.order)

    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'لیست جزئیات سبد خرید'
        