from django.conf.urls import patterns, include, url#default


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       #url(r'^pools/$',include('pools.urls')),
                       url(r'^$','openshift.views.index', name='index'),
                       url(r'two.html/$','openshift.views.two',name='two')
                       
                       #url(r'^admin/',include(admin.site.urls)),
                       
    # Examples:
    # url(r'^$', 'tester.views.home', name='home'),
    # url(r'^tester/', include('tester.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
 
