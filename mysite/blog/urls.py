from django.conf.urls import include, url
from . import views
from django.contrib import admin


urlpatterns = [
    #Post views
    url(r'^$',views.post_list, name='post_list'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<blog>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^admin/', include(admin.site.urls)),
]

