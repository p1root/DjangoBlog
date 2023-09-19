from django.urls import path
from blog.views import (HomeListView,
                        Detail_View,
                        CategoryListView,
                        Preview_View,
                        about,
                        contact,
                        SearchListView)

urlpatterns = [
    path("" , HomeListView.as_view() , name="home"),
    path("about" , about , name="about"),
    path("contactUs" , contact , name="contact"),
    path("article/<slug:slug>" , Detail_View.as_view() , name="detail"),
    path("article/preview/<slug:slug>" , Preview_View.as_view() , name="preview"),
    path("category/<slug:slug>" , CategoryListView.as_view() , name="category"),
    path("search/" , SearchListView.as_view() , name="search"),
]