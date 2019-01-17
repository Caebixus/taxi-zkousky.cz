from django.urls import path, include
from . import views

urlpatterns = [
    path('Exam1', views.exams, name='Exam1'),
    path('Exam2', views.Exam2, name='Exam2'),
    path('Exam3', views.Exam3, name='Exam3'),
    path('Exam4', views.Exam4, name='Exam4'),
    path('Exam5', views.Exam5, name='Exam5'),
    path('Exam6', views.Exam6, name='Exam6'),
    path('Exam7', views.Exam7, name='Exam7'),
    path('Exam8', views.Exam8, name='Exam8'),
    path('Exam9', views.Exam9, name='Exam9'),
    path('Exam10', views.Exam10, name='Exam10'),
    path('Exam11', views.Exam11, name='Exam11'),
    path('Exam12', views.Exam12, name='Exam12'),
    path('Exam13', views.Exam13, name='Exam13'),
    path('Exam14', views.Exam14, name='Exam14'),
    path('Exam15', views.Exam15, name='Exam15'),
    path('SearchTest', views.searchTest, name='SearchTest'),
]
