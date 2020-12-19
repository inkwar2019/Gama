from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views as user_views
from .views import SupportCreate


urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='user/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'),name='logout'),
    path('profile/',user_views.profile,name='profile'),
    path('support/',SupportCreate.as_view(),name='support'),
    path('contact/',user_views.contact,name='contact')
]

