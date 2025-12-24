"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),  # ЭТА СТРОКА ОБЯЗАТЕЛЬНО ДОЛЖНА БЫТЬ
]

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse  # Добавьте эту строку

def home_view(request):
    return HttpResponse("""
        <h1>ToDo API работает! 🎉</h1>
        <p>Доступные эндпоинты:</p>
        <ul>
            <li><a href="/api/tasks/">API задач (GET/POST)</a></li>
            <li><a href="/admin/">Админ-панель Django</a></li>
        </ul>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('tasks.urls')),
    path('', home_view),  # Добавьте эту строку для корневого URL
]