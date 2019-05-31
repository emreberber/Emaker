from django.conf.urls import url
from .views import *

app_name = 'exam'

urlpatterns=[
    url(r'^$', view=index, name='index'),
    url(r'^create/$', view=create, name='create'),
    url(r'^update/(?P<id>[0-9]+)$', view=update, name='update'),
    url(r'^delete/(?P<id>[0-9]+)$', view=delete, name='delete'),
    url(r'^(?P<id>[0-9]+)$', view=exam, name='exam'),
	url(r'^(?P<id>[0-9]+)$', view=exam, name='exam'),

]