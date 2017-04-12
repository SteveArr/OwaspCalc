from django.conf.urls import url
from owaspcalc.views import *

from . import views

app_name='owaspcalc'
urlpatterns = [
    url(r'^$', views.list, name='index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit, name='edit'),
    url(r'^delete/(?P<pk>\d+)/$', RiskAuditDelete.as_view(), name='delete'),
    url(r'^detail/(?P<slug>[\w-]+)/$', views.detail, name='detail'),
]