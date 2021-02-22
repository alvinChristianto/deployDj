from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^all_data', views.show_data, name='list-data'),
]