from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows/', views.showsAll),
    path('shows/new', views.go_create),
    path('createShow', views.create_show),
    path('delete/<_id>', views.delete_show),
    path('shows/<_id>', views.readOne),
    path('shows/<_id>/edit', views.go_edit),
    path('shows/<_id>/update', views.edit_show),
]