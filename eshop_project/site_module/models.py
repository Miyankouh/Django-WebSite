from django.db import models


class SiteSetting(models.Model):
    site_name = models.CharField(max_length=255, verbose_name='نام سایت')
    site_url = models.CharField(max_length=255, verbose_name='دامنه سایت')
    address = models.CharField(max_length=255, verbose_name='ادرس ')
    phone = models.CharField(max_length=255, null=True, blank=True, verbose_name='تلفن ')
    fax = models.CharField(max_length=255, null=True, blank=True, verbose_name='فاکس ')
    email = models.CharField(max_length=255, null=True, blank=True, verbose_name='ایمیل')
    copy_right = models.CharField(max_length=255, verbose_name='متن کپی رایت ,سایت')
    about_us_text = models.TextField(verbose_name=' متن درباره ما سایت')
    site_logo = models.ImageField(upload_to='images/site_setting/', verbose_name='لوگوی سایت')
    is_main_setting = models.BooleanField(verbose_name='تنظیمات اصلی')

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = 'تنضیمات سایت '
        verbose_name_plural = ' تنظیمات'
        
    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    url = models.URLField(max_length=250 , verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = '  لینک  فوتر'
        verbose_name_plural = '   لینک های فوتر'

    def __str__(self):
        return self.title


class Slider(models.Model):
    title = models.CharField(max_length=255, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='ادرس')
    url_title = models.CharField(max_length=100, verbose_name=' عنوان لینک ')
    description = models.TextField(max_length=255, verbose_name='توضیحات  اسلایدر')
    image = models.ImageField(upload_to='images/sliders', verbose_name='تصویر اسلایدر')
    is_active = models.BooleanField(default=True, verbose_name='فعال / غیر فعال')

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name ='اسلایدر'
        verbose_name_plural = 'اسلایدر ها'

    def __str__(self):
        return self.title
        