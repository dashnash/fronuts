from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fronuts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', lambda r : HttpResponseRedirect('fronuts/')),
    url(r'^fronuts/', include('fronuts_app.urls', namespace='fronuts' ))
)
