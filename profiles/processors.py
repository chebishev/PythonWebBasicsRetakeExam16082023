from profiles.models import ProfileModel


def profile(request):
    try:
        profile_exists = ProfileModel.objects.all().first()
    except IndexError:
        profile_exists = None
        return {'profile_exists': profile_exists}
