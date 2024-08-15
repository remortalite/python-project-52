from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin

from statuses.models import Status
from statuses.forms import StatusForm


class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        statuses = Status.objects.all()
        return render(request, "statuses/index.html",
                      context={"statuses": statuses})


class StatusCreateView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        form = StatusForm()
        return render(request, "statuses/create.html",
                      {"form": form})

    def post(self, request, *args, **kwargs):
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _("Статус успешно создан"))
            return redirect(reverse("statuses"))
        return render(request, "statuses/create.html",
                      {"form": form})


class StatusUpdateView(LoginRequiredMixin, View):

    def get(self, request, id, *args, **kwargs):
        status = get_object_or_404(Status, id=id)
        form = StatusForm(instance=status)
        return render(request, "statuses/update.html",
                      context={"form": form, "status_id": id})

    def post(self, request, id, *args, **kwargs):
        status = get_object_or_404(Status, id=id)
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.info(request, _("Статус успешно изменен"))
            return redirect(reverse("statuses"))
        return render(request, "statuses/update.html",
                      {"form": form, "status_id": id})


class StatusDeleteView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        status = get_object_or_404(Status, id=id)
        return render(request, "statuses/delete.html",
                      context={"status_id": id, "status": status})

    def post(self, request, id, *args, **kwargs):
        status = get_object_or_404(Status, id=id)
        if status.task_set.exists():
            messages.error(request, _("Невозможно удалить статус, "
                                      "потому что он используется"))
        else:
            status.delete()
            messages.info(request, _("Статус успешно удален"))
        return redirect(reverse("statuses"))
