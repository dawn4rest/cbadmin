from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from post import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/', include('post.urls', namespace='post')),
    url(r'^comment/', include('comment.urls', namespace='comment')),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^admin/', admin.site.urls),
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
