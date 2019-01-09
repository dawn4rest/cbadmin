from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^mypage/$', views.my_page, name='my_page'),
    url(r'^password_change/$', views.password_change, name='password_change'),
    url(r'^delete/$', views.user_delete, name='user_delete'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^log/$', views.user_log, name='user_log'),
    url(r'^contact/create/$', views.create_chat, name='create_chat'),
    url(r'^get_liked_posts/$', views.get_liked_posts, name='get_liked_posts'),
    url(r'^toggle/$', views.get_toggle, name='get_toggle'),
]
