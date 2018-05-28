from django.urls import re_path, path
from rango import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    path('about/', views.about, name='about'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    re_path(r'^add_category/$', views.add_category, name='add_category'),
]
