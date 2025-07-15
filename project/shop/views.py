from django.shortcuts import render

from .models import BookProduct

# Create your views here.


def home_page(request):
    books = BookProduct.objects.all()
    return render(request, "home.html", {"books": books})
