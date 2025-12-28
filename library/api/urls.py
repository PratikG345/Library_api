from django.urls import path
from .views import get_book,create_book,update_book

urlpatterns = [
    path('',get_book,name="get_book"),
    path('create/',create_book,name="create_book"),
    path('<int:pk>/',update_book,name="update_book"),
]