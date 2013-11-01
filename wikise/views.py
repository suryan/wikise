'''
Created on 30-Oct-2013

@author: suryan
'''

from django import shortcuts
from django import template
import requests
import re
from wikiapi import fetch

def index(request):
    if request.method == "POST":
        wiki_url = request.POST.get('wiki_url')
        if len(re.findall(r'http://en.wikipedia.org/wiki/[a-zA-Z0-9_]+',
                          wiki_url)) != 1 :
            error_message = 'Wrong URL Format'
            return shortcuts.render_to_response('index.html', locals(),
                            context_instance=template.RequestContext(request))
        
        article = wiki_url.replace('http://en.wikipedia.org/wiki/','')
        data = fetch(article)
        revision_ids = []
        if data['error'] == 0 :
            revision_ids = data['id']
        else :
            error_message = data['error']
    return shortcuts.render_to_response('index.html', locals(),
                            context_instance=template.RequestContext(request))