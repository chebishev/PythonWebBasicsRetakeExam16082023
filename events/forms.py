from django import forms

from events.models import EventModel


class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = "__all__"
