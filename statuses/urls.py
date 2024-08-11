from django.urls import path

from statuses.views import (IndexView, StatusCreateView,
                            StatusUpdateView, StatusDeleteView)

urlpatterns = [
    path('', IndexView.as_view(), name="statuses"),
    path('create/', StatusCreateView.as_view(), name="statuses_create"),
    path('<int:id>/update/',
         StatusUpdateView.as_view(),
         name="statuses_update"),
    path('<int:id>/delete/',
         StatusDeleteView.as_view(),
         name="statuses_delete"),
]
