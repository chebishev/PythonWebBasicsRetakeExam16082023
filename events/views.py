from django.shortcuts import render, redirect

from events.forms import EventForm
from events.models import EventModel


# Create your views here.
def create_event(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'events/event-create.html', {'form': form})


def event_details(request, id):
    event = EventModel.objects.get(id=id)
    return render(request, 'events/events-details.html', {'event': event})


def edit_event(request, id):
    event = EventModel.objects.get(id=id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'events/event-edit.html', {'form': form})


def delete_event(request, id):
    event = EventModel.objects.get(id=id)
    form = EventForm(request.POST or None, instance=event)
    for field in form.fields.values():
        field.widget.attrs['disabled'] = 'disabled'
    if request.method == 'POST':
        event.delete()
        return redirect('dashboard')

    return render(request, 'events/events-delete.html', {'form': form})
