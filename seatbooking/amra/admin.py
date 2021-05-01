from django.contrib import admin

from .models import Theatre, Movie, Seat, Timing

admin.site.register(Theatre)
admin.site.register(Movie)
admin.site.register(Seat)
admin.site.register(Timing)
