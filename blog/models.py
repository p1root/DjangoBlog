from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.template.defaultfilters import truncatechars
from account.models import User
from django.utils.html import format_html
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

class CategoryManager(models.Manager):
    def publishd(self):
        return self.filter(status=True)
    
class ArticleManager(models.Manager):
    def publishd(self):
        return self.filter(status="W")


class IP_Address(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آیپی') 
    
    def __str__(self) -> str:
        return self.ip_address
class Category(models.Model):
    category  = models.ForeignKey("self" , on_delete= models.CASCADE ,null=True , blank=True,verbose_name="زیر مجموعه", related_name="parent",related_query_name="children")
    title = models.CharField("نام" , max_length=80)
    slug = models.SlugField(max_length=100 , unique=True, verbose_name="هدف")
    status = models.BooleanField(verbose_name="نمایش",default=True)
    createDate = models.DateTimeField(auto_now_add=True )
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name = "گروه"
        verbose_name_plural = "گروه ها"
    objects = CategoryManager()

class Article(models.Model):
    user = models.ForeignKey(User , null=True , verbose_name="نویسنده" , on_delete=models.CASCADE , related_name="articles")
    title = models.CharField(max_length=100 , verbose_name="موضوع")
    slug = models.SlugField(max_length=100 , unique=True, verbose_name="هدف")
    decription = models.TextField("متن")
    createDate = models.DateTimeField(auto_now_add=True )
    publsihDate = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    updateDate = models.DateField(auto_now=True)
    picture = models.ImageField(upload_to="images/Articles" , verbose_name="تصویر")
    status = models.CharField(max_length=1,choices=[("I" , "پیش نویس") , ("W" , "نوشته شده")] , verbose_name="وضعیت")
    category = models.ManyToManyField(Category , related_name="Article")
    is_special = models.BooleanField(blank=True , default=False ,verbose_name="مقاله وِیژه" )
    comments = GenericRelation(Comment)
    IPs = models.ManyToManyField(IP_Address , related_name='article' , blank=True)
    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def get_absolute_url(self):
        return reverse("account:home")
    
    objects = ArticleManager()
    @property
    def short_decription(self):
        return truncatechars(self.decription, 100)
    def __str__(self) -> str:
        return self.title
    
    def show_image(self):
        return format_html(f"<img width=100 height=100 src='{self.picture.url}'></img>")
    
