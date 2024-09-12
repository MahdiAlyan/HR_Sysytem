from django.urls import path
from . import views

urlpatterns = [
    path('HR/', views.index, name='HR'),
]
