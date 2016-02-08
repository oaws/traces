from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tapi/$', views.tapi, name='tapi'),
    url(r'^sentiment/$', views.sentiment, name='sentiment'),
	url(r'^twsent/$', views.twsent, name='twsent'),
]