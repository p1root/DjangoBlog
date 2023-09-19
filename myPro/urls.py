"""
URL configuration for myPro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from django.urls import include
from blog import urls
from account import urls as account_urls
from django.contrib.auth import views as auth_views
from account.views import Login,signup,activate

urlpatterns = [
    path("login/", Login.as_view(), name="login"),
    path("signup/", signup.as_view(), name="signup"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('admin/', admin.site.urls),
    path('',include((urls.urlpatterns , "blog") , namespace="blog")),
    path('account/',include((account_urls.urlpatterns,"account") , namespace="account")),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
    activate, name='activate'),
    path('admin/', admin.site.urls),
    path('comment/', include('comment.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)