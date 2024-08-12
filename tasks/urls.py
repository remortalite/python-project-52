from django.urls import path, include

from tasks import views

urlpatterns = [
    path('', views.TasksView.as_view(), name="tasks"),
    path('create/', views.TasksCreateView.as_view(), name="tasks_create"),
    path('<int:id>/', views.TasksShowView.as_view(), name="tasks_show"),
    path('<int:id>/update', views.TasksShowView.as_view(), name="tasks_update"),
    path('<int:id>/delete', views.TasksShowView.as_view(), name="tasks_delete"),
]