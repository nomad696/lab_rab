"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from webapp.views import index_view, create_view, delete_view, change_status_view, remove_done_tasks_view, edit_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view, name='index'),
    path('task/create', create_view, name='task_create'),
    path('task/<int:task_pk>/delete', delete_view, name='task_delete'),
    path('task/<int:task_pk>/change/<str:status>', change_status_view, name='change_status'),
    path('task/done/remove', remove_done_tasks_view, name="remove_done_tasks"),
    path('task/<int:task_pk>/edit', edit_view, name='edit_view'),
]
