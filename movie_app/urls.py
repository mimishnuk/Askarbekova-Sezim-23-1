from django.contrib import admin
from django.urls import path, include
from movie_app.views import *

list_create = {
    'get': 'list',
    'post': 'create'}

update_retrieve_destroy = {
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'}

urlpatterns = [
    path('directors/', DirectorModelViewSet.as_view(list_create)),
    path('directors/<int:pk>/', DirectorModelViewSet.as_view(update_retrieve_destroy)),
    path('movies/', MovieModelViewSet.as_view(list_create)),
    path('movies/<int:id>/', MovieModelViewSet.as_view(update_retrieve_destroy)),
    path('reviews/', ReviewModelViewSet.as_view(list_create)),
    path('reviews/<int:pk>/', ReviewModelViewSet.as_view(update_retrieve_destroy)),
    path('movies/reviews/', ReviewMovieListAPIView.as_view()),

]
