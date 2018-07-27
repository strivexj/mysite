from django.conf.urls import url

from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^app.json$', views.timetable, name='timetable'),
]
