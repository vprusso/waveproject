from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from upload import urls as upload_urls

from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^upload/', include(upload_urls)),
    url(r'^$', RedirectView.as_view(url='/upload/list_files/')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)