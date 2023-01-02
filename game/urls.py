from django.urls import path
from . import views
urlpatterns = [
    path('main_page/', views.main_page),
    path('singleplayer/', views.singleplayer),
    path('multiplayer/', views.multiplayer),
    path('register/', views.register),
    path('login/', views.login),
    path('finishregistration/', views.finishregistration)
]