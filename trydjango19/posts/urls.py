from django.conf.urls import url
from django.contrib import admin

# from posts import views
from . import views
from .views import (post_create,post_list,post_detail,post_delete,post_update)

# urlpatterns = [
#     # url(r'^$', views.post_home),
#     url(r'^create$', "posts.views.post_create"),
#     url(r'^detail/$', "posts.views.post_detail"),
#     url(r'^$', "posts.views.post_list"),
#     url(r'^update/$', "posts.views.post_update"),
#     url(r'^delete/$', "posts.views.post_delete"),
# ]

urlpatterns = [
    # url(r'^$', views.post_home),
    url(r'^create/$', post_create),
    # url(r'^(?P<pk>\d+)/$', post_detail,name='detail'),
    url(r'^$', post_list, name='list'),
    # url(r'^(?P<pk>\d+)/edit/$', post_update, name='update'),
    # url(r'^(?P<pk>\d+)/delete/$', post_delete),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]