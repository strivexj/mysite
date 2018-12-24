from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app.json$', views.timetable, name='timetable'),
    url(r'^glossary$', views.tv_series_list, name='tv_series_list'),
    url(r'^list$', views.list, name='list'),
    url(r'linkGameRanking', views.linkGameRanking, name='linkGameRanking'),

    url(r'adaptationList$', views.adaptation_list, name='adaptation_list'),
    url(r'^adaptationform$', views.adaptation_form, name='adaptation_form'),
    url(r'^adaptationdetail/(?P<id>\d+)$', views.adaptation_detail, name='adaptation_detail'),
]
