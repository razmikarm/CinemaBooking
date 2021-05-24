from django.contrib import admin

from .models import Theatre, Movie, Timing, Booking

admin.site.register(Theatre)
admin.site.register(Movie)
admin.site.register(Timing)
admin.site.register(Booking)
