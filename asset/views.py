from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html', RequestContext(request))


def idc(request):
    return render_to_response('asset_idc.html', RequestContext(request))


def asset(request):
    return render_to_response('asset_list.html', RequestContext(request))