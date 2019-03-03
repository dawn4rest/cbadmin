from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^views/$', views.post_list_views, name='post_list_views'),
    url(r'^comments/$', views.post_list_comments, name='post_list_comments'),
    url(r'^likes/$', views.post_list_likes, name='post_list_likes'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'^(?P<post_pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<post_pk>\d+)/update/$', views.post_update, name='post_update'),
    url(r'^(?P<post_pk>\d+)/delete/$', views.post_delete, name='post_delete'),

    url(r'^(?P<post_pk>\d+)/share-count/$',
        views.add_share_count, name='add_share_count'),
    url(r'^(?P<post_pk>\d+)/like-toggle/$',
        views.post_like_toggle, name='post_like_toggle'),
    url(r'^category/(?P<hierarchy>.+)/$', views.show_category, name='category'),
    url(r'^category/(?P<hierarchy>.+)/views$',
        views.show_category_views, name='show_category_views'),
    url(r'^category/(?P<hierarchy>.+)/comments$',
        views.show_category_comments, name='show_category_comments'),
    url(r'^category/(?P<hierarchy>.+)/likes$',
        views.show_category_likes, name='show_category_likes'),
    url(r'^search/$', views.search, name='search'),
]
