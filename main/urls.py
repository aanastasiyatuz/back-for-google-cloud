from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from myprofile.views import ProviderViewSet, ClientViewSet
from facilities.views import PlaceViewSet, CateringViewSet, LodgingViewSet

'''-------SWAGGER---------'''
schema_view = get_schema_view(
   openapi.Info(
      title="Travel Startup API",
      default_version='v1',
      description="Travel Startup",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router_provider = DefaultRouter()
router_provider.register('', ProviderViewSet)
router_client = DefaultRouter()
router_client.register('', ClientViewSet)

router_facilities = DefaultRouter()
router_facilities.register('place', PlaceViewSet)
router_facilities.register('catering', CateringViewSet)
router_facilities.register('lodging', LodgingViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('account/', include('account.urls')),
    path('profile_provider/', include(router_provider.urls)),
    path('profile_client/', include(router_client.urls)),
    path('', include(router_facilities.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)