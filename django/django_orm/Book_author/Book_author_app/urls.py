from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path('AddBook', views.AddBook, name='add_book'),
    path('books/<int:book_id>/', views.InfoBook, name='info_book'),
    path('deleteBook/<int:book_id>/', views.delete, name='delete_book'),
    path('AddAuthor_Book/<int:book_id>/', views.AddAuthor_Book, name='add_author_book'),
   
    path('authors',views.author),
    path('AddAuthor', views.AddAuthor),
    path('authors/<int:author_id>', views.InfoAuthor),
    path('delete_author/<int:author_id>', views.delete_author, name='delete_author'),
    path('AddBook_Author/<int:author_id>', views.AddBook_Author),
    ]