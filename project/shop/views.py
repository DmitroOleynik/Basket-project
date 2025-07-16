from django.shortcuts import render
from django.core.paginator import Paginator

from .models import BookProduct

# Create your views here.


def home_page(request):
    if not request.session.session_key:
        request.session["nonuser"] = True
        request.session.save()

    books = BookProduct.objects.all()
    paginator = Paginator(books, 3)

    page_num = request.GET.get('page', 1)
    page = paginator.get_page(page_num)

    context = {
        'books': page
    }

    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html")


def book_page(request, article):
    book = BookProduct.objects.get(pk=article)
    return render(request, "book.html", {"book": book})
