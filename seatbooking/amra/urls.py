from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:theatre_id>/', views.detail, name='detail'),
    # ex: /polls/5/movies/
    path('<int:theatre_id>/movies/', views.movies, name='movies'),
]