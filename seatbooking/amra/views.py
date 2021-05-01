from django.http import HttpResponse

from .models import Theatre


def index(request):
    all_halls = Theatre.objects.all()
    output = ', '.join([thtr.name for thtr in all_halls])
    return HttpResponse(output)


def detail(request, theatre_id):
    thtr = Theatre.objects.get(pk=1)
    return HttpResponse(thtr)


def movies(request, theatre_id):
    response = "You're looking at the movies in theatre %s."
    return HttpResponse(response % theatre_id)
