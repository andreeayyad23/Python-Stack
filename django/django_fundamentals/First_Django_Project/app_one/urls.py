
from django.urls import path ,include
from . import views
urlpatterns = [
     path('blogs', views.index),
     path('',views.root),
     path('blogs/new', views.new),
     path('blogs/create',views.create),
     path('blogs/<int:number>',views.show),
     path('blogs/<int:number>/edit',views.edit),
     path('blogs/<int:number>/delete',views.destroy)
]
