from django import views
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from task_manager.forms import UserCreateForm, UserUpdateForm


class IndexView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


class LoginView(views.View):
    def get(self, request, *args, **kwargs):
        return render(request, "registration/login.html")

    def post(self, request, *args, **kwargs):
        username = request.POST.get("loginUsername")
        password = request.POST.get("loginPassword")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, _("Вы залогинены"))
            return render(request, "index.html")

        messages.error(request, _("Пожалуйста, введите правильные имя пользователя и пароль. "
                                  "Оба поля могут быть чувствительны к регистру."))
        return render(request,
                      "registration/login.html",
                      context={"username": username},
                      status=403)


class LogoutView(views.View):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.info(request, _("Вы разлогинены"))
        return redirect(reverse("index"))


class UsersView(views.View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, "users.html", context={"users": users})


class UserFormView(views.View):
    def get(self, request, *args, **kwargs):
        form = UserCreateForm()
        return render(request, "registration/signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _("Пользователь успешно зарегистрирован"))
            return redirect(reverse('login'))
        return render(request, "registration/signup.html", {"form": form})


class UserUpdateView(LoginRequiredMixin, views.View):
    login_url = '/login/'
    def get(self, request, id, *args, **kwargs):
        if request.user.id != id:
            messages.error(request, _("У вас нет прав для изменения другого пользователя."))
            return redirect(reverse('users'))
        user = User.objects.get(id=id)
        form = UserUpdateForm(instance=user)
        if user:
            return render(request, "registration/update.html", {"form": form, "user_id": id})

    def post(self, request, id, *args, **kwargs):
        if request.user.id != id:
            messages.error(request, _("У вас нет прав для изменения другого пользователя."))
            return redirect(reverse('users'))
        user = User.objects.get(id=id)
        form = UserUpdateForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, _("Пользователь успешно изменен"))
            return redirect(reverse('index'))
        return render(request, "registration/update.html", {"form": form, "user_id": id})

class UserDeleteView(LoginRequiredMixin, views.View):
    login_url = "/login/"
    def get(self, request, id, *args, **kwargs):
        if request.user.id != id:
            messages.error(request, _("У вас нет прав для изменения другого пользователя."))
            return redirect(reverse('users'))
        user = User.objects.get(id=id)
        return render(request, "registration/delete.html", {"user": user})

    def post(self, request, id, *args, **kwargs):
        if request.user.id != id:
            messages.error(request, _("У вас нет прав для изменения другого пользователя."))
            return redirect(reverse('users'))
        user = User.objects.get(id=id)
        if user:
            user.delete()
            messages.info(request, _("Пользователь успешно удален"))
        return redirect(reverse("users"))
