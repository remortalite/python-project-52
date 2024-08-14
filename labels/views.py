from django.shortcuts import render
from django.views import View

from labels.models import Label

class IndexView(View):
    def get(self, request, *args, **kwargs):
        labels = Label.objects.all()
        return render(request,
                      "labels/index.html",
                      {"labels": labels})
