from django.urls import path
from labels import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="labels"),
    path('create/', views.CreateLabelView.as_view(), name="labels_create"),
]
