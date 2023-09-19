# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
class User(AbstractUser):
    address = models.CharField("ادرس", max_length=50 , blank=True)
    special_suer = models.DateTimeField(default=timezone.now,verbose_name="کاربر ویژه تا")
    picture = models.ImageField(upload_to='media/images/users/' , verbose_name='تصویر', default='/images/users/account.png' , blank=True)
    def is_special_user(self):
        return self.special_suer > timezone.now()
    is_special_user.short_description = "کاربر ویژه"
    is_special_user.boolean = True
    
    def is_author(self):
        return len(self.articles.all()) != 0
    is_author.boolean = True
    is_author.short_description = "نویسنده"