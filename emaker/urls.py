from django.conf.urls import url,include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import *
from lesson.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index , name='homepage'),
    url(r'^exam/', include('exam.urls', namespace='exam')),
    url(r'^lesson/', include('lesson.urls', namespace='lesson')),
    url(r'^question/', include('question.urls', namespace='question')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),

]+static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)