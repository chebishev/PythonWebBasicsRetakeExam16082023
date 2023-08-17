from django.shortcuts import render, redirect

from events.models import EventModel
from profiles.forms import ProfileCreateForm, ProfileEditForm
from profiles.models import ProfileModel


# Create your views here.
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'profiles/profile-create.html', {'form': form})


def profile_details(request):
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile,
        'events': EventModel.objects.all()
    }
    return render(request, 'profiles/profile-details.html', context)


def profile_edit(request):
    profile = ProfileModel.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile_details')

    return render(request, 'profiles/profile-edit.html', {'form': form})


def profile_delete(request):
    # ProfileModel.objects.first() gets one profile, but we may have more and after deletion
    # we will not be redirected to the home page without profile
    # profile = ProfileModel.objects.first()
    profiles = ProfileModel.objects.all()
    events = EventModel.objects.all()
    if request.method == 'POST':
        profiles.delete()
        events.delete()
        return redirect('index')
    return render(request, 'profiles/profile-delete.html')
