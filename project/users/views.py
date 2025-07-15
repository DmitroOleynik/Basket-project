from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from .forms import LoginUserForm, RegisterUser

# Create your views here.


def register_user(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("home"))
        else:
            return redirect(reverse("register"))

    form = RegisterUser()

    return render(request, "register.html", context={"form": form})


def login_page(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username=clean_data["username"], password=clean_data["password"])

            if user and user.is_active:
                login(request, user)
                return redirect(reverse("home"))

    else:
        form = LoginUserForm()
    return render(request, "login.html", {"form": form})


def logout_page(request):
    logout(request)
    return redirect(reverse("home"))
