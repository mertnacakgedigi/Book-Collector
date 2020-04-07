from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  # route for cats index
  path('books/', views.books_index, name='index'),
  path('books/<int:book_id>/', views.books_detail, name='detail'),
  path('cats/<int:book_id>/add_rating/', views.add_rating, name='add_rating'),
]