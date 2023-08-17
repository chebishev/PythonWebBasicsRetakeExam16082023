from django.shortcuts import render

from events.models import EventModel


# Create your views here.
def index(request):
    return render(request, 'shared/home-page.html')


def dashboard(request):
    events = EventModel.objects.all()
    return render(request, 'events/dashboard.html', {'events': events})
