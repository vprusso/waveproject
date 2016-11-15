from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list_files/$', views.list_files, name='list_files'),
]
