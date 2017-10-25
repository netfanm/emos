from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import IDC


def index(request):
    return render_to_response('index.html', RequestContext(request))


def idc(request):
    data = {}
    idc_info = IDC.objects.get()

    data = {
        'idc_info':idc_info
    }

    return render_to_response('asset_idc.html', data, RequestContext(request))


def idc_add(request):
    return render_to_response('asset_idc_add.html', RequestContext(request))


def idc_edit(request):
    return render_to_response('asset_idc_edit.html', RequestContext(request))


def idc_del(request):
    return render_to_response('asset_idc_add.html', RequestContext(request))


def asset(request):
    return render_to_response('asset_list.html', RequestContext(request))