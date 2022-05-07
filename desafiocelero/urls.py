from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="120 years of Olympic history: athletes and results ",
      default_version='v1',
      description="",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('olympics/', include('olympics.urls', namespace='olympics')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='docs'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

