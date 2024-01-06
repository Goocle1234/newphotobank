from django.urls import path,include
from .views import register

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),  # login, logout
    path('register/', register, name='register'),
]