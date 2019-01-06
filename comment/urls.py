from django.conf.urls import url

from . import views


urlpatterns = [
    # Comment Url
    url(r'^(?P<comment_pk>\d+)/$', views.comment_detail, name='comment_detail'),
    url(r'^(?P<post_pk>\d+)/create/$',
        views.comment_create, name='comment_create'),
    url(r'^(?P<comment_pk>\d+)/update/$',
        views.comment_update, name='comment_update'),
    url(r'^delete/$', views.comment_delete, name='comment_delete'),

    # Comment on Comment Url
    url(r'^coc/(?P<coc_pk>\d+)/$', views.coc_detail, name='coc_detail'),
    url(r'^coc/$', views.coc_create, name='coc_create'),
    url(r'^coc/(?P<coc_pk>\d+)/update/$',
        views.coc_update, name='coc_update'),
    url(r'^coc/delete/$', views.coc_delete, name='coc_delete'),

    # Comment action Url
    url(r'^like-toggle/$', views.comment_like_toggle, name='comment_like_toggle'),
    url(r'^hate-toggle/$', views.comment_hate_toggle, name='comment_hate_toggle'),
    url(r'^(?P<comment_pk>\d+)/report/$',
        views.comment_report, name='comment_report'),
    url(r'^coc/(?P<coc_pk>\d+)/report/$', views.coc_report, name='coc_report'),
]
