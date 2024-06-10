from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('registration',views.registration),
    path('login',views.login),
    path('dashboard', views.dashboard),
    path('add_magazine', views.add_magazine),
    path('magazines/new', views.go_create),
    path('magazine/<int:_id>', views.info_magazine),
    path('user/account', views.edit),
    path('update_user', views.edit_user),
    path('delete/<int:_id>/', views.delete_title),

    path('logout/', views.logout_view, name='logout'),
]