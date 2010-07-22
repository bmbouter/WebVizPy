from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def simple(request):
    width = 800
    height = 400
    return render_to_response('WebVizPy/timeseries.htm',
            {'width': width, 'height' : height},
        context_instance=RequestContext(request))

def table(request):
    return render_to_response('WebVizPy/table.htm',{'width' : 800, 'height' : 800},
        context_instance=RequestContext(request))
