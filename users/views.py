from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.db.models.deletion import ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from users.models import User
from users.forms import UserForm
from users.mixins import (UserOnlyEditThemselfPermissionMixin,
                          LoginRequiredWithMessageMixin)


class UserListView(ListView):
    model = User


class UserCreateView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    success_message = _("User created")
    success_url = reverse_lazy("login")


class UserUpdateView(LoginRequiredWithMessageMixin,
                     UserOnlyEditThemselfPermissionMixin,
                     SuccessMessageMixin,
                     UpdateView):
    model = User
    form_class = UserForm
    success_url = fail_url = reverse_lazy("users")
    template_name_suffix = "_update"

    success_message = _("User updated")
    no_auth_message = _("First you need to log in!")
    fail_message = _("You can't edit another user")


class UserDeleteView(LoginRequiredWithMessageMixin,
                     UserOnlyEditThemselfPermissionMixin,
                     SuccessMessageMixin,
                     DeleteView):
    model = User
    success_url = reverse_lazy("users")
    fail_url = reverse_lazy("users")

    success_message = _("User deleted")
    fail_message = _("You can't update another user")
    no_auth_message = _("First you need to log in!")

    def post(self, request, pk, *args, **kwargs):
        try:
            data = super().post(request, pk, *args, **kwargs)
        except ProtectedError:
            messages.error(request, _("Unable to delete user"))
            return redirect(reverse("users"))
        return data
