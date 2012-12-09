from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.core.urlresolvers import reverse

import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',


    url(r'^accounts/logout/', redirect_to, {'url':'/'}),                  # by default, users will be directed here after they logout
    url(r'^users/.*', redirect_to, {'url':'/home/'}),                     # by default, users will be directed here after registration

    url(r'^accounts/', include('registration.backends.simple.urls')),     # django-registration "simple" backend system. Does NOT require working email server
    # url(r'^accounts/', include('registration.backends.default.urls')),  # django-registration "default" backend system. Requires working email server
    
    url(r'^home/', 'myfirstapp.views.home'),                              # first app url
    url(r'^admin/', include(admin.site.urls)),                            # URL for admin area


    url(r'.*', redirect_to, {'url':'/accounts/login/'}),                    # by default, all other urls will send the user to the login page

    # serve media, should be used in development only
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL, 'show_indexes': True}),
)
