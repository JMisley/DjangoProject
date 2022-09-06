from django.urls import path

from movie import views

urlpatterns = [
    path('', views.index, name='mo_home'),
    path('addmovie', views.addMovie, name='mo_add_movie'),
]
