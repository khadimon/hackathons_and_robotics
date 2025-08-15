from django.urls import path
from .views import *  # Import your views

urlpatterns = [
    path('admin-login/', admin_login, name='admin-login'), 
    path('admin-home/', admin_home, name='admin-home'), 
]
