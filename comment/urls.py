from django.conf.urls import url

from . import views


urlpatterns = [
    # Comment Url
    url(r'^procomment/(?P<comment_pk>\d+)/$', views.pro_comment_detail, name='pro_comment_detail'),
    url(r'^concomment/(?P<comment_pk>\d+)/$', views.con_comment_detail, name='con_comment_detail'),
    url(r'^(?P<post_pk>\d+)/procomment/create/$', views.pro_comment_create, name='pro_comment_create'),
    url(r'^(?P<post_pk>\d+)/concomment/create/$', views.con_comment_create, name='con_comment_create'),
    url(r'^procomment/(?P<comment_pk>\d+)/update/$', views.pro_comment_update, name='pro_comment_update'),
    url(r'^concomment/(?P<comment_pk>\d+)/update/$', views.con_comment_update, name='con_comment_update'),
    url(r'^procomment/(?P<comment_pk>\d+)/delete/$', views.pro_comment_delete, name='pro_comment_delete'),
    url(r'^concomment/(?P<comment_pk>\d+)/delete/$', views.con_comment_delete, name='con_comment_delete'),

    # Comment action Url
    url(r'^(?P<comment_pk>\d+)/comment-pro-comment/$', views.comment_pro_comment, name='comment_pro_comment'),
    url(r'^(?P<comment_pk>\d+)/comment-con-comment/$', views.comment_con_comment, name='comment_con_comment'),
    url(r'^(?P<comment_pk>\d+)/pro-report/$', views.pro_comment_report, name='pro_comment_report'),
    url(r'^(?P<comment_pk>\d+)/con-report/$', views.con_comment_report, name='con_comment_report'),

    url(r'^(?P<comment_pk>\d+)/like-pro-toggle/$', views.pro_comment_like_toggle, name='pro_comment_like_toggle'),
    url(r'^(?P<comment_pk>\d+)/like-con-toggle/$', views.con_comment_like_toggle, name='con_comment_like_toggle'),
    url(r'^(?P<comment_pk>\d+)/hate-pro-toggle/$', views.pro_comment_hate_toggle, name='pro_comment_hate_toggle'),
    url(r'^(?P<comment_pk>\d+)/hate-con-toggle/$', views.con_comment_hate_toggle, name='con_comment_hate_toggle'),
]
