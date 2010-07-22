from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def timeseries(request):
    width = 800
    height = 400
    return render_to_response('WebVizPy/timeseries.htm',
            {'width': width, 'height' : height},
        context_instance=RequestContext(request))

def table(request):
    width = 80
    height = 80
    return render_to_response('WebVizPy/table.htm',{'width' : width, 'height' : height},
        context_instance=RequestContext(request))

def map(request):
    width = 800
    height = 400
    return render_to_response('WebVizPy/map.htm',
            {'width': width, 'height' : height},
        context_instance=RequestContext(request))
