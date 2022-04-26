from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    avatar = models.CharField(max_length=255, verbose_name='تصویر اواتار', null=True, blank=True)
    email_active_code = models.CharField(max_length=150, verbose_name='کد فعال سازی ایمیل')

    # The meta class is for displaying the title in the admin panel
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        if self.first_name is not '' and self.last_name is not '':
            return self.get_full_name()
        return self.email
