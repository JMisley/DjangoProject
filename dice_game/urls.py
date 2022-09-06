from django.urls import path

from dice_game import views

urlpatterns = [
    path('dice_game', views.index, name='dg_home'),
    path('results', views.results, name='results')
]
