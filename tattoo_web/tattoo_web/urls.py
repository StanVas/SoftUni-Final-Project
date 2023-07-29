from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tattoo_web.common.urls')),
    path('photos/', include('tattoo_web.photos.urls')),
    path('accounts/', include('tattoo_web.accounts.urls')),
    path('articles/', include('tattoo_web.articles.urls')),
]

# 9XkxsTh^y5D5!2gPy&Vn