from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dance', views.dance, name='dance'),
    path('about', views.about, name='about'),
]