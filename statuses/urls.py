from django.urls import path

from statuses.views import IndexView, StatusCreateView, StatusUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name="statuses"),
    path('create/', StatusCreateView.as_view(), name="statuses_create"),
    path('<int:id>/update/',
         StatusUpdateView.as_view(),
         name="statuses_update"),
]
