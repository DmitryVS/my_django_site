from django.urls import path, re_path 
from . import views
from .views import PostDetailView

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^nasledie/$', views.post_list, name='post_list'),
	re_path(r'^nasledie/block/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='block-detail'),
	re_path(r'^post/new/$', views.post_new, name='post_new'),
]