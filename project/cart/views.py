from django.db.models import F
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Order
from shop.models import BookProduct

# Create your views here.


def cart(request):
    if not request.session.session_key:
        request.session["nonuser"] = True
        request.session.save()

    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user.id)
    else:
        anonim = request.session.session_key
        orders = Order.objects.filter(user=anonim)

    total_price = sum([order.book_product.price * order.count for order in orders])

    return render(request, "cart.html", {"orders": orders, "total": total_price})


def add_to_cart(request, article):
    if not request.session.session_key:
        request.session["nonuser"] = True
        request.session.save()

    if request.method == "POST":
        _id = ""
        if request.user.is_authenticated:
            _id = str(request.user.id)
        else:
            _id = request.session.session_key

        book_product = get_object_or_404(BookProduct, pk=article)

        order, created = Order.objects.get_or_create(
            user=_id,
            book_product=book_product,
            defaults={'count': 1}
        )

        if not created:
            order.count = order.count + 1
            order.save()

        return redirect(reverse("cart"))
    return redirect(reverse("cart"))


def del_order(request, article):
    if not request.session.session_key:
        request.session["nonuser"] = True
        request.session.save()

    if request.method == "POST":
        _id = ""
        if request.user.is_authenticated:
            _id = str(request.user.id)
        else:
            _id = str(request.session.session_key)

        order = Order.objects.filter(user=_id, book_product=BookProduct.objects.get(pk=article)).first()
        order.delete()

        return redirect(reverse("cart"))
    return redirect(reverse("cart"))


def del_one_order(request, article):
    if not request.session.session_key:
        request.session["nonuser"] = True
        request.session.save()

    if request.method == "POST":
        _id = ""
        if request.user.is_authenticated:
            _id = str(request.user.id)
        else:
            _id = str(request.session.session_key)

        order = Order.objects.filter(user=_id, book_product=BookProduct.objects.get(pk=article)).first()

        if order.count > 1:
            order.count = order.count - 1
            order.save()

        return redirect(reverse("cart"))
    return redirect(reverse("cart"))
