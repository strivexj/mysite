from django.conf.urls import url
from django.contrib.auth.views import *

from user import views

urlpatterns = [
    url(r'^login/$', login, {'template_name': 'account/login.html'},
        name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.register, name='register'),

    url(r'^password-change/$', password_change,
        {"post_change_redirect": "/account/password-change-done"}, name='password_change'),
    url(r'^password-change-done/$', password_change_done, name='password_change_done'),

    url(r'^password-reset/$', password_reset,
        {"post_reset_redirect": "/account/password-reset-done"}
        , name='password_reset'),
    url(r'^password-reset-done/$', password_reset_done, name='password_reset_done'),

    url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        password_reset_confirm, {"template_name": "account/password_reset_confirm.html",
                                 "post_reset_redirect": "/account/password-reset-complete"},
        name="password_reset_confirm"),

    # url(r'^password-reset-confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
    #     {"post_reset_redirect": "/account/password-reset-complete"}
    #     , name='password_reset_confirm'),

    url(r'^password-reset-complete/$', password_reset_complete, name='password_reset_complete'),
]
