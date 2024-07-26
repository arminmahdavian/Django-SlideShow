from django.shortcuts import render
from .models import SlideShow


# Create your views here.


def home(request):
    context = {
        "slides": SlideShow.objects.filter(status=True, article__status=True),
    }
    return render(request, 'SlideShow/home.html', context)

