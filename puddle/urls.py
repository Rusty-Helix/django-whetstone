from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core.views import detail
# from core import views.index

# app_name = 'item' # create namespace

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('items/<int:pk>/', detail, name='detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
