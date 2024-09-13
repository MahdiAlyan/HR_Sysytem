from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users/create user/', views.create_user, name='create_user'),
    path('users/edit user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('users/delete user/<int:user_id>/', views.delete_user, name='delete_user'),

]
