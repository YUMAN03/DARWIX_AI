from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('generate/', views.generate_titles_view, name='generate_titles'),
]

# title_app/apps.py
from django.apps import AppConfig

class TitleAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'title_app'

# title_app/admin.py
from django.contrib import admin
from .models import TitleRequest

admin.site.register(TitleRequest)
