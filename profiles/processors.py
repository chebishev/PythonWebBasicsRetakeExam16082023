from profiles.models import ProfileModel


def profile(request):
    return {'profile': ProfileModel.objects.all()}
