from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response

def simple(request):
    a = 0
    return render_to_response('WebVizPy/simple.htm',
        {'some_variable': a, },
        context_instance=RequestContext(request))
