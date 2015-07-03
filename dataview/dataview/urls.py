from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from testapi.api import SampleResource

from testapi import views

sample_resource = SampleResource()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dataview.views.home', name='home'),
    # url(r'^dataview/', include('dataview.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^api/', include(sample_resource.urls)),
    url(r'^search/', include('haystack.urls')),
    # url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
    #     'document_root':'E:\PythonPrograms\\tastipye\dataview-proj\dataview\static'
    # }),
)