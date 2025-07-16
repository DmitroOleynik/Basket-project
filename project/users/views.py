from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import FormView
from django.urls import reverse
from django.contrib.auth.models import User

from .forms import LoginUserForm, UserRegistrationForm


# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return redirect(reverse("login"))
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'form': user_form})


def login_page(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            clean_data = form.cleaned_data
            user = authenticate(request, username=clean_data["username"], password=clean_data["password"])

            if user:
                login(request, user)
                return redirect(reverse("home"))

    else:
        form = LoginUserForm()
    return render(request, "login.html", {"form": form})


def logout_page(request):
    logout(request)
    return redirect(reverse("home"))
