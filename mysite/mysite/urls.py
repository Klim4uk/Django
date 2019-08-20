from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('news/', include("news.urls")),
    re_path(r'^accounts/', include('allauth.urls')),
    path('ticket/', include("ticket.urls")),
    path('summernote/', include('django_summernote.urls')),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

