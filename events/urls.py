from django.urls import path
from .views import create_event, event_details, edit_event, delete_event

urlpatterns = [
    path('create', create_event, name='create_event'),
    path('details/<int:id>/', event_details, name='event_details'),
    path('edit/<int:id>/', edit_event, name='edit_event'),
    path('delete/<int:id>/', delete_event, name='delete_event'),
]
