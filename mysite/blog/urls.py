#coding: utf-8
from django.conf.urls import patterns, url
from blog.views import PostListView, PostDetailview

urlpatterns = patterns(
    '',
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', PostDetailview.as_view())
)
