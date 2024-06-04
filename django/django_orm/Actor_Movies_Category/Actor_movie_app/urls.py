from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('movie/<int:_id>/', views.movie_detail, name='movie_detail'), 
]