from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('new_todo', views.new_todo, name="new_todo")
]