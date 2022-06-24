from django.urls import path
from . import views

urlpatterns = {
    path('', views.index),
    path('menu/',views.menu),
    path('book/',views.book),
    path('about/',views.about),
}