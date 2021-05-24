from django import forms
from django.db import models

from django.contrib.auth.models import User


class Theatre(models.Model):
    name = models.TextField()
    seat_row_count = models.IntegerField()
    seats_in_row = models.IntegerField()

    def seats(self):
        return (
            tuple(self.bookings.filter(seat_row=row, seat_number=number).first()
                  for number in range(1, self.seat_row_count + 1)
            ) for row in range(1, self.seats_in_row + 1)
        )

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.TextField()
    poster_path = models.TextField(null=True)
    # duration
    # price

    def __str__(self):
        return self.name


class Timing(models.Model):
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name='timings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField()  # Can create separate table, if times are fixed


class Booking(models.Model):
    timing = models.ForeignKey(Timing, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name="bookings")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    seat_row = models.IntegerField()
    seat_number = models.IntegerField()
