from django import views
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.translation import gettext_lazy as _


class IndexView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "task_manager/index.html")


class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "task_manager/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("loginUsername")
        password = request.POST.get("loginPassword")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, _("You logged in"))
            return redirect(reverse('index'))

        messages.error(request, _("Please enter correct username and password. "
                                  "Both fields are case sensitive"))
        return render(request,
                      "task_manager/login.html",
                      context={"username": username},
                      status=400)


class LogoutView(views.View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _("You logged out"))
        return redirect(reverse("index"))
