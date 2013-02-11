# handler404 and handler500 are needed for admin tests
from guardian.compat import include, patterns, handler404, handler500
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)


