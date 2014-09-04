from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.base import View
from django.contrib.auth.models import User, Group



def index(request):
	return render(request,'index.html');


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)



class DashboardView(LoggedInMixin, View):

    template_name = 'dashboard.html'
    
    def get(self, request):
    	is_athlon = request.user.groups.filter(name='athlon')
    	is_calpolyrec = request.user.groups.filter(name='calpolyrec')
    	is_kennedyfitness = request.user.groups.filter(name='kennedyfitness')

        return render(request,'dashboard.html', {'is_athlon': is_athlon, 'is_calpolyrec': is_calpolyrec, 'is_kennedyfitness': is_kennedyfitness});
