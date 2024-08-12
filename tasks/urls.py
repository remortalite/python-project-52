from django.urls import path, include

from tasks import views

urlpatterns = [
    path('', views.TasksView.as_view(), name="tasks"),
]