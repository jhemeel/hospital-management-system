from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include



app_name = 'administrators'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrators.urls', namespace='administrators')),
    path('', include('authy.urls')),
    path('', include('base.urls')),
    path('', include('doctors.urls')),
    path('', include('laboratory.urls')),
    path('', include('nurses.urls')),
    path('', include('patients.urls')),
    path('', include('profiles.urls')),
    path('', include('reception.urls')),
    
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/', include('allauth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)