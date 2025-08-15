from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('user/', views.user_view, name='user'),
    path('Admin/', views.admin_view, name='admin'),
]
