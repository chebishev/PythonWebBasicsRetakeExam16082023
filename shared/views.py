from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'shared/home-page.html')


def dashboard(request):
    return render(request, 'events/dashboard.html')