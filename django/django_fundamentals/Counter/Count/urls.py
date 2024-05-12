from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('addtwo', views.addTwo),
    path('destroy_session', views.Reset),
]