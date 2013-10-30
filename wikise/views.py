'''
Created on 30-Oct-2013

@author: suryan
'''

from django import shortcuts
from django import http
from django import template


def index(request):
    message = "Hello World"
    return shortcuts.render_to_response('index.html', locals(),
                                        context_instance=template.RequestContext(request))