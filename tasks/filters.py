import django_filters

from django.forms.widgets import CheckboxInput

from tasks.models import Task


class TasksFilter(django_filters.FilterSet):
    author = django_filters.BooleanFilter(method="is_author",
                                          widget=CheckboxInput(),
                                          field_name="author")

    class Meta:
        model = Task
        fields = ["status", "assigned_to", "labels"]

    def is_author(self, queryset, name, value):
        author = getattr(self.request, 'user', None)
        if value:
            return queryset.filter(author=author)
        return queryset
