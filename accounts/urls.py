from django.conf.urls import url
from .views import *

app_name = 'accounts'

urlpatterns=[
    url(r'^login/$', view=login_user, name='login'),
    url(r'^register/$', view=register_user, name='register'),
    url(r'^logout/$', view=logout_user, name='logout'),
    url(r'^profile/$', view=profile, name='profile'),
    url(r'^profile-photo/$', view=profile_photo, name='profile_photo'),

]