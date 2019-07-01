from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from Asistencia import views

urlpatterns = [
    re_path(r'asistencia_lista/$', views.AsistenciaList.as_view()),
    re_path(r'asistencia_detail/(?P<id>\d+)/$',views.AsistenciaDetail.as_view()),
]