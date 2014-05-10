from django.conf.urls import patterns, include, url
from demo.app import DemoView

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'$', DemoView.as_view(), name='demo'),
)
