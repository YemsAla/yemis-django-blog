# about/urls.py

from . import views
from django.urls import path
from .views import about_page

urlpatterns = [
    path('', views.about_page, name='about'),
]
