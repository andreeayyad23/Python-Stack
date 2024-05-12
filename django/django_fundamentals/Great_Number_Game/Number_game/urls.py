from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('correct', views.correct),
    path('process', views.process),
    path('too_high', views.too_high),
    path('too_low', views.too_low),
]