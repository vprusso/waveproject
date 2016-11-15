from django.conf.urls import url
from upload.views import list_files

urlpatterns = [
    url(r'^list_files/$', list_files, name='list_files'),
]