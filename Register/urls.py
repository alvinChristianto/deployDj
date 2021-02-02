from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^register/$', views.index_register, name='register'),
	url(r'^listuser/$', views.listuser, name='listuser'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^login_invalid/$', views.login_invalid_view, name='login_invalid'),

    url(r'^sent/$', views.activation_sent_view, name="activation_sent"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name="activate"),
    url(r'^activation-success/$', views.activation_success_view, name="activation-success"),
    url(r'^index/success_login/$', views.success_login, name='success_login'),
	url(r'^logout/$', views.user_logout, name="user_logout"),
]