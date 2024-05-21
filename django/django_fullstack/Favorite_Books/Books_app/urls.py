from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('registration',views.registration),
    path('login',views.login),
    path('books', views.book_home),
    path('add_book', views.add_book),
    path('<int:_id>/', views.info_book),
    path('un_favorite/<int:_id>', views.un_favorite),
    path('favorite/<int:_id>', views.favorite),
    path('update/<int:_id>',views.update),
    path('delete/<int:_id>/',views.delete_book ),
    path('logout', views.logout),
]