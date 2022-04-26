from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ProductCategory(models.Model):
    title = models.CharField(
        max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(
        max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def __str__(self):
        return f"( {self.title} - {self.url_title})"

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class ProductBrand(models.Model):
    title = models.CharField(
        max_length=300, verbose_name='نام برند', db_index=True)
    is_active = models.BooleanField(verbose_name='فعال / غیر فعال')

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = 'برند'
        verbose_name_plural = 'برند ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان محصول')
    category = models.ManyToManyField(
        ProductCategory,
        related_name='product_categories',
        verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/products', null=True, blank=True, verbose_name='تصویر محصول')
    brand = models.ForeignKey(
                ProductBrand,
                on_delete=models.CASCADE,
                verbose_name='برند',
                null=True, blank=True
    )
    price = models.IntegerField(verbose_name='قیمت')
    short_description = models.TextField(
        null=True, db_index=True, verbose_name='توضیح کوتاه')
    description = models.TextField(
        null=True,  db_index=True, verbose_name='توضیح اصلی')
    is_active = models.BooleanField(
        default=False, verbose_name='فعال / غیر فعال')
    slug = models.SlugField(
        default='',
        null=False,
        db_index=True,
        blank=True,
        max_length=255,
        unique=True,
        verbose_name='عنوان در url'
    )
    is_delete = models.BooleanField(verbose_name='حذف شده / نشده')

    def get_absolute_url(self):
        return reverse('product-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = ' محصول'
        verbose_name_plural = '  محصول ها'


class ProductTag(models.Model):
    caption = models.CharField(
        max_length=300, db_index=True, verbose_name='تگ')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product_tags')

    def __str__(self):
        return self.caption

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = 'تگ محصول'
        verbose_name_plural = 'تگ های محصولات'
