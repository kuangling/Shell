from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'salt_ui.views.home', name='home'),
    # url(r'^salt_ui/', include('salt_ui.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^admin/', include(admin.site.urls)),
      url(r'^index/','salt_ui.salt.views.index'),
      url(r'^login/','salt_ui.salt.views.login'),
)
