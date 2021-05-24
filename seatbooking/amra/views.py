import pytz
from django.db.models import Q
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Theatre, Timing, Booking


def index(request):
    print(request.user)
    theatres = Theatre.objects.all()
    context = {'theatres': theatres}
    return render(request, 'amra/index.html', context)


def movies(request, theatre_id):
    current_time = timezone.now()
    theatre = get_object_or_404(Theatre, pk=theatre_id)
    timings = theatre.timings.filter(Q(show_time__gt=current_time))
    context = {
        'header': theatre.name,
        'timings': timings,
        }
    return render(request, 'amra/movies.html', context)


def details(request, timing_id):
    print(request.user)
    timing = get_object_or_404(Timing, pk=timing_id)
    seats = timing.theatre.seats()
    context = {
        'seats': seats,
        'timing': timing,
        }
    return render(request, 'amra/details.html', context)


@login_required(login_url='/account/login/')
def book(request, timing_id, seat_row, seat_number):
    timing = get_object_or_404(Timing, pk=timing_id)
    if (0 < seat_row <= timing.theatre.seat_row_count
            and 0 < seat_number <= timing.theatre.seats_in_row):
        bookings = timing.theatre.bookings.filter(seat_row=seat_row, seat_number=seat_number)
        if not bookings:
            booking = Booking()
            booking.timing = timing
            booking.theatre = timing.theatre
            booking.user = request.user
            booking.seat_row = seat_row
            booking.seat_number = seat_number
            booking.save()
    return HttpResponseRedirect(f'/session/{timing_id}/')
