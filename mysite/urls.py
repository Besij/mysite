from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


import blog.views 

urlpatterns = [
    path('', blog.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
