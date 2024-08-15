import django_filters

from tasks.models import Task


class TasksFilter(django_filters.FilterSet):
    class Meta:
        model = Task
        fields = ["status", "assigned_to", "labels"]
