from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('' , include('Main.urls')),
    path('Visitor/' , include('visitor.urls')),
    path('Event/' , include('event.urls')),
    path('ControlPanel/' , include('ControlPanel.urls')),
    path('webpush/' , include('webpush.urls')),
    path('', include('pwa.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
