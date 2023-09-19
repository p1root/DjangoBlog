from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
UserAdmin.fieldsets+= (
                        ("وضعیت کاربر", {"fields": ("special_suer",)}),
                        ("ادرس", {"fields": ("address",'picture')})
                        ,)
UserAdmin.list_display+=("is_author","is_special_user","address",)
admin.site.register(User, UserAdmin)