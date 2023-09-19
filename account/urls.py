from django.urls import path
from .views import (ArticleList,
                    ArticleCreate,
                    ArticleUpdate,
                    ProfileUpdate,
                    ArticleDelete,)
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path("", ArticleList.as_view(), name="home"),
    path("create/", ArticleCreate.as_view(), name="article-create"),
    path("update/<int:pk>", ArticleUpdate.as_view(), name="article-update"),
    path("profile/", ProfileUpdate.as_view(), name="profile"),
    path("delete/<int:pk>", ArticleDelete.as_view(), name="article-delete"),  
]
#passwoord  
# urlpatterns += [
#     path("password_change/", auth_views.PasswordChangeView.as_view(), name="password_change"),
#     path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
#     path("password_reset/", auth_views.PasswordResetView.as_view(), name="password_reset"),
#     path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
#     path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
#     path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
# ]
