from django.http import Http404, HttpResponse
import pytz
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models import Theatre, Timing, Movie


def index(request):
    theatres = Theatre.objects.all()
    context = {'theatres': theatres}
    return render(request, 'amra/index.html', context)


def details(request, timing_id):
    timing = get_object_or_404(Timing, pk=timing_id)
    movie = timing.movie
    seats = timing.theatre.seats.all()
    context = {
        'movie': movie,
        'seats': seats,
        }
    return render(request, 'amra/details.html', context)


def movies(request, theatre_id):
    current_time = timezone.now()
    theatre = get_object_or_404(Theatre, pk=theatre_id)
    timings = theatre.timings.filter(Q(show_time__gt=current_time))
    context = {
        'header': theatre.name,
        'timings': timings,
        }
    return render(request, 'amra/movies.html', context)
