"""sigxinapi URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
urlpatterns = [
    path("", include("sigxinapp.urls")),
    path('admin/', admin.site.urls),
]
