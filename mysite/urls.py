from django.conf.urls import patterns, include, url
from django.contrib import admin
from portal.admin import admin_site
from mysite.views import *
urlpatterns = patterns('',
(r'^$',main_page),
#login/logout
(r'^login/$','django.contrib.auth.views.login'),
(r'^logout/$',logout_page),
#signup
(r'^signup/$',signup_page),
url(r'^myadmin/', include(admin_site.urls)),
#web portal
(r'^portal/',include('portal.urls')),
 # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   url(r'^admin/', include(admin.site.urls)),
url(r'^like_category/$',like_category),
url(r'^accept_page/$',accept_page),
url(r'^search/$',search_page),
url(r'^room/$',room_page),
url(r'^get_room/$',get_room),
url(r'^reject/$',reject_page),
url(r'^available/$',available_page),
url(r'^pass_recovery/$',pass_recovery),
)
