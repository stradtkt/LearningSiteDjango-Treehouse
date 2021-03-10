
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^suggest/$', views.suggestion_view, name='suggestion'),
    url(r'^$', views.hello_world, name='home'),
]

urlpatterns += staticfiles_urlpatterns()
