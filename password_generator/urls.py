from django.urls import path, include
from password_generator import views

urlpatterns = [
    path('', views.index, name='pw_home'),
    path('result/', views.result, name='pw_result'),
]
