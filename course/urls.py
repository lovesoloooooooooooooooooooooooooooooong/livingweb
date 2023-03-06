from django.conf.urls import url, include
from . import views as api_views
from rest_framework.authtoken import views

urlpatterns = [
    url(r'^coursedeatil', api_views.CourseDeatilApi.as_view(), name='coursedeatil'),
    url(r'^subscribe', api_views.UserCourselApi.as_view(), name='subscribe'),
    url(r'^issubscribe', api_views.issubscribeAPI.as_view(), name='issubscribe'),
    url(r'^record', api_views.geturlApi.as_view(), name='record')
]