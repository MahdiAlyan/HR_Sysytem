from django.urls import path
from . import views

urlpatterns = [
    path('Home/', views.Home, name='Home'),
    path('profile/<int:user_id>/', views.profile, name='profile'),
    path('profile/edit-picture/', views.edit_profile_pic, name='edit_profile_pic'),
    path('profile/remove-pic/', views.remove_profile_pic, name='remove_profile_pic'),
    path('upload_profile_pic/', views.upload_profile_pic, name='upload_profile_pic'),

]

