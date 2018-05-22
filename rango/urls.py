from django.urls import re_path, path
from rango import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('about/', views.about, name='about'),
]
