from django.contrib import admin
from django.urls import path, re_path
from converter.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/', ConvertVideo.as_view(), name='convert-video'),
    path('get-video-info/', VideoInfo.as_view(), name='get-video-info'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
