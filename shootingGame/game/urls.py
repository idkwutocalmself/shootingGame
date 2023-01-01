from django.urls import path
from . import views
urlpatterns = [
    path('main_page/', views.main_page),
    path('singleplayer/', views.singleplayer),
    path('multiplayer/', views.multiplayer)
]