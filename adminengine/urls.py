from django.conf.urls import patterns, url
from adminengine import views

urlpatterns = patterns('',

	url(r'^$', views.index, name='index'),

	#auth URLs
	url(r'^login/$', 'django.contrib.auth.views.login', name='login'),

    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login/'}, name='logout'),
    
    url(r'^dashboard/$', views.TrafficView.as_view(), name='dashboard'),
	url(r'^membership/$', views.MembershipView.as_view(), name='membership'),
   


)