from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app.json$', views.timetable, name='timetable'),
    url(r'^glossary$', views.tv_series_list, name='tv_series_list'),
    url(r'^list$', views.list, name='list'),

    url(r'^requestadaptation$', views.requestAdaptation, name='requestadaptation'),

    url(r'linkGameRanking', views.linkGameRanking, name='linkGameRanking'),

    url(r'adaptationList$', views.adaptation_list, name='adaptation_list'),
    url(r'^adaptationform$', views.adaptation_form, name='adaptation_form'),
    url(r'^adaptationdetail/(?P<id>\d+)$', views.adaptation_detail, name='adaptation_detail'),
    url(r'^valid/(?P<id>\d+)$', views.valid, name='valid'),
    url(r'^adapted/(?P<id>\d+)$', views.adapted, name='adapted'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),

    url(r'^adaptationapi$', views.adaptationapi, name='adaptationapi'),

    url(r'^v2ray$', views.v2ray, name='v2ray'),
]
