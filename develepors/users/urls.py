from django.urls import path
from . import views

urlpatterns = [
    path('register_page',views.register_page,name="register_page"),
    path('login_page',views.login_page,name="login_page"),
    path('log_out',views.log_out,name="log_out"),
    path('',views.profile,name="profile"),
    path('user_profile/<str:pk>/',views.user_profile,name="user_profile"),
    path('user_account',views.user_account,name="user_account"),
    path('edit_account',views.edit_account,name="edit_account")
]
