from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
]
