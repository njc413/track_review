from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = patterns('',
   url(r'^$', Home.as_view(), name='home'),
   url(r'^user/',include('registration.backends.simple.urls')),
   url(r'^user/',include('django.contrib.auth.urls')),
   url(r'^review/create/$', login_required(ReviewCreateView.as_view()), name='review_create'),
   url(r'review/$', login_required(ReviewListView.as_view()), name='review_list'),
   url(r'^review/(?P<pk>\d+)/$', login_required(ReviewDetailView.as_view()), name='review_detail'),
   url(r'^review/update/(?P<pk>\d+)/$', login_required(ReviewUpdateView.as_view()), name='review_update'),
   url(r'^review/delete/(?P<pk>\d+)/$', login_required(ReviewDeleteView.as_view()), name='review_delete'),
   url(r'^review/(?P<pk>\d+)/reply/create/$', login_required(ReplyCreateView.as_view()), name='reply_create'),
   url(r'^review/(?P<review_pk>\d+)/reply/update/(?P<reply_pk>\d+)/$', login_required(ReplyUpdateView.as_view()),name='reply_update'),
   url(r'^review/(?P<review_pk>\d+)/reply/delete/(?P<reply_pk>\d+)/$', login_required(ReplyDeleteView.as_view()), name='reply_delete'),
 )