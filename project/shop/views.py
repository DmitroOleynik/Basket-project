from django.shortcuts import render

from .models import BookProduct

# Create your views here.


def home_page(request):
    if not request.session.session_key:
        request.session["nonuser"] = True
        request.session.save()

    books = BookProduct.objects.all()
    return render(request, "home.html", {"books": books})


def about_page(request):
    return render(request, "about.html")


def book_page(request, article):
    book = BookProduct.objects.get(pk=article)
    return render(request, "book.html", {"book": book})
