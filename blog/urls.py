from django.urls import path, re_path, include
from . import views

app_name = 'blog'

urlpatterns = [
    re_path(r'^$', views.post_list, name='post_list'),
    re_path(r'^(?P<id>\d+)/$', views.post_detail, name='post_detail')
]