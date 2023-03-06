from django.conf.urls import url, include
from . import views as api_views
from rest_framework.authtoken import views

urlpatterns = [

    url(r'api-token-auth', views.obtain_auth_token),#登录
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),#注册
    url(r'^userdetail/$', api_views.UserDetailAPI.as_view(), name='userdetail'),
    # url(r'^rtmToken/$', api_views.UserDetailAPI.as_view(), name='rtmToken'),
    url(r'^rtmToken/$', api_views.GetRtmTokenAPI.as_view(), name='rtmToken'),


]