from django.shortcuts import render, redirect

from profiles.forms import ProfileCreateForm


# Create your views here.
def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'profiles/profile-create.html', {'form': form})


def profile_details(request):
    return None


def profile_edit(request):
    return None


def profile_delete(request):
    return None
