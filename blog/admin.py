from django.contrib import admin
from blog.models import (Article ,
                            Category ,
                            IP_Address
                              )

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title" ,"show_image","user", "createDate", "status" , "get_categris"]
    list_filter = ["title","status","createDate","publsihDate","category"]
    def get_categris(self, obj):
        return " ".join(["#" +str(c)for c in obj.category.all()])

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title" ,"category"]
    list_filter = ["status","category"]


admin.site.register(Article , ArticleAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(IP_Address)