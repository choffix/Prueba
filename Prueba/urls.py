from django.conf.urls import patterns, include, url
from Prueba1.views import current_datetime

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Prueba.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^time/$', current_datetime),
)
