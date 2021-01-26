from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^register/$', views.index_register, name='index_register'),
    url(r'^listuser/$', views.listuser),

    url(r'^sent/$', views.activation_sent_view, name="activation_sent"),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name="activate"),
    url(r'^index/success_login/$', views.success_login, name='success_login'),
	url(r'^logout/$', views.user_logout, name="user_logout"),
]