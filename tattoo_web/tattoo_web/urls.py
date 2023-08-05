from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tattoo_web.common.urls')),
    path('photos/', include('tattoo_web.photos.urls')),
    path('accounts/', include('tattoo_web.accounts.urls')),
    path('articles/', include('tattoo_web.articles.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# 9XkxsTh^y5D5!2gPy&Vn
