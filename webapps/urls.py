from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('project/', views.newProject, name="project"),
    path('wordpress/', views.wordpress, name="wordpress"),
    path('ghost/', views.ghost, name="ghost"),
]
