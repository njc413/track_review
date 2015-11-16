from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/',include('registration.backends.simple.urls')),
   url(r'^user/',include('django.contrib.auth.urls')),
   url(r'^review/create/$', ReviewCreateView.as_view(), name='review_create'),
   url(r'review/$', ReviewListView.as_view(), name='review_list'),
   url(r'^review/(?P<pk>\d+)/$', ReviewDetailView.as_view(), name='review_detail'),
 )