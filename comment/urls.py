from django.conf.urls import url

from . import views


urlpatterns = [
    # Comment Url
    url(r'^(?P<comment_pk>\d+)/$', views.comment_detail, name='comment_detail'),
    url(r'^(?P<post_pk>\d+)/create/$', views.comment_create, name='comment_create'),
    url(r'^(?P<comment_pk>\d+)/update/$', views.comment_update, name='comment_update'),
    url(r'^delete/$', views.comment_delete, name='comment_delete'),

    # Comment action Url
    url(r'^(?P<comment_pk>\d+)/comment-on-comment/$', views.comment_on_comment, name='comment_on_comment'),
    url(r'^(?P<comment_pk>\d+)/report/$', views.comment_report, name='comment_report'),

    url(r'^(?P<comment_pk>\d+)/like-toggle/$', views.comment_like_toggle, name='comment_like_toggle'),
    url(r'^(?P<comment_pk>\d+)/hate-toggle/$', views.comment_hate_toggle, name='comment_hate_toggle'),
]
