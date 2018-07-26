from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$', views.blog_titile, name='blog_titile'),
    url(r'^(?P<article_id>\d+)/$', views.blog_article, name='blog_article'),
]
