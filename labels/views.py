from django.shortcuts import render, reverse, redirect
from django.views import View
from django.contrib import messages
from django.utils.translation import gettext as _

from labels.models import Label
from labels.forms import LabelForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request,
                      "labels/index.html",
                      {"labels": labels})


class CreateLabelView(View):
    def get(self, request, *args, **kwargs):
        form = LabelForm()
        return render(request,
                      "labels/create.html",
                      {"form": form})

    def post(self, request, *args, **kwargs):
        form = LabelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, _("Метка успешно создана"))
            return redirect(reverse("labels"))
        return render(request,
                      "labels/create.html",
                      {"form": form})
