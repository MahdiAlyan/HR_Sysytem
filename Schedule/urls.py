from django.urls import path
from . import views

urlpatterns = [
    path('', views.Schedule, name='Schedule'),
    path('request-day-off/', views.request_day_off, name='request_day_off'),
    path('check_in/', views.check_in, name='check_in'),
    path('check_out/', views.check_out, name='check_out'),
]
