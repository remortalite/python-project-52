"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task_manager.views import LoginView, LogoutView, UsersView

from task_manager import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('users/', views.UsersView.as_view(), name="users"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('signup/', views.IndexView.as_view(), name="signup"),
    path('users/<int:id>/update', views.IndexView.as_view(), name="user_update"),
    path('users/<int:id>/delete', views.IndexView.as_view(), name="user_delete"),
]
