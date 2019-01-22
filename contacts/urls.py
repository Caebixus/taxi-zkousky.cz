from django.urls import path, include
from . import views

urlpatterns = [
    path('hodnoceni', views.hodnoceni, name='hodnoceni'),
]
