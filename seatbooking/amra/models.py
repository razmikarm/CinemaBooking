from django import forms
from django.db import models


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField(max_length=40)
    password = forms.CharField(min_length=8, max_length=20, widget=forms.PasswordInput)

    def __str__(self):
        return self.first_name


class Theatre(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Seat(models.Model):  # Can be implemented in Theatre as matrix
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE, related_name='seats')
    row = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return f"{self.row}|{self.number}"


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
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
