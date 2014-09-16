from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.base import View
from django.contrib.auth.models import User, Group

from firebase import firebase


def index(request):
	return render(request,'index.html');


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)



class TrafficView(LoggedInMixin, View):
    
    def get(self, request):

        # store the user's group in a variable
    	user_group = request.user.groups.all()[0].name

        # get visits data from firebase
        visits = retrieveVisits(firebase, user_group);

        return render(request,'adminhome.html', {'request':request, 'user_group': user_group, 'visits': visits});



class MembershipView(LoggedInMixin, View):
    
    def get(self, request):

        # store the user's group in a variable
    	user_group = request.user.groups.all()[0].name

        # get users data from firebase
        users = retrieveUsers(firebase, user_group);

        return render(request,'adminmembership.html', {'request':request, 'user_group': user_group, 'users': users});


# Firebase - Retrieve Visits
def retrieveVisits(firebase, group):
    firebase = firebase.FirebaseApplication('https://hellobeacon.firebaseio.com', None)
    result = firebase.get('/Gyms/' + group + '/Visits/', None)
    return result;

# Firebase - Retrieve Users
def retrieveUsers(firebase, group):
    firebase = firebase.FirebaseApplication('https://hellobeacon.firebaseio.com', None)
    result = firebase.get('/Gyms/' + group + '/Users/', None)
    return result;