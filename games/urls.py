from django.conf.urls import url 
from games import views
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/games/filter$', views.filter),
    url(r'^api/games/autocomplete/(?P<keyword>[\w\-]+)$', views.auto_complete),
    url(r'^api/game/(?P<id>[0-9]+)$', views.detail),
    url(r'^api/game/(?P<id>[0-9]+)/history$', views.history),
    url(r'^api/game/(?P<id>[0-9]+)/contracts$', views.contracts),
    url(r'^api/siteinfo$', views.site_info),
]