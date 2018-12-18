from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app.json$', views.timetable, name='timetable'),
    url(r'^glossary$', views.tv_series_list, name='tv_series_list'),
    url(r'list$', views.list,name='list'),
]
