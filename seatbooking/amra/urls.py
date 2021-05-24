from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /5/movies/
    path('<int:theatre_id>/movies/', views.movies, name='movies'),
    # ex: /5/movies/2
    path('session/<int:timing_id>/', views.details, name='details'),
    # ex: /5/movies/2
    path('book/<int:timing_id>/<int:seat_row>/<int:seat_number>/', views.book, name='book'),
]