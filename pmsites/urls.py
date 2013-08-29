from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pmsites.views.home', name='home'),
    # url(r'^pmsites/', include('pmsites.foo.urls')),
    url(r'^$', 'pm.views.home'),
    url(r'^cources/(?P<id>\d+)/$', 'pm.views.cource'),
    url(r'^cources/(?P<id>\d+)/schedule/$', 'pm.views.schedule'),
    url(r'^cources/(?P<id>\d+)/progress/$', 'pm.views.progress'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
