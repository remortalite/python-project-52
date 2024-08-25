from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from statuses.models import Status


class StatusListView(LoginRequiredMixin, ListView):
    model = Status


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    fields = ["name"]
    success_url = reverse_lazy("statuses")

    def post(self, request, *args, **kwargs):
        messages.info(request, _("Статус успешно создан"))
        return super().post(self, request, *args, **kwargs)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    fields = ["name"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("statuses")

    def post(self, request, *args, **kwargs):
        messages.info(request, _("Статус успешно изменен"))
        return super().post(self, request, *args, **kwargs)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    success_url = reverse_lazy("statuses")

    def post(self, request, *args, **kwargs):
        messages.info(request, _("Статус успешно удален"))
        return super().post(self, request, *args, **kwargs)
