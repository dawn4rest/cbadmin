from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from . import views
from post import views as post_views


urlpatterns = [
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^comment/', include('comment.urls', namespace='comment')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^admin/', admin.site.urls),

    url(r'^$', post_views.post_list, name='post_list'),
    url(r'^company/$', views.get_company, name='get_company'),
    url(r'^guide/$', views.get_guide, name='get_guide'),
    url(r'^term/$', views.get_term, name='get_term'),
    url(r'^privacy/$', views.get_privacy, name='get_privacy'),

]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
