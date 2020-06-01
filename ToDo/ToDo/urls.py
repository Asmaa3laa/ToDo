"""ToDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.views.generic import TemplateView
from to_do import views as todo_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', todo_view.list_tasks),
    path('save/', todo_view.save_task),
    path('delete/', todo_view.delete_task),
    # path('tasks/', TemplateView.as_view(template_name='todo_list.html')),
]











