from django.conf.urls import patterns, url
from adminengine import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),

	#auth URLs
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
)