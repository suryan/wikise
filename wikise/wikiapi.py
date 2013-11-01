'''
Created on 01-Nov-2013

@author: suryan
'''

import requests
import xml.etree.ElementTree as ET

def fetch(article) :
    xmlns = "{http://www.mediawiki.org/xml/export-0.8/}"
    params = {'title' :'Special:Export', 'action' : 'submit',
                  'pages' : article, 'catname' : '', 'wpDownload' : '1'}
    try:
        resp = requests.post('http://en.wikipedia.org/w/index.php', params = params)
    except requests.exceptions.RequestException as e:
        return {'error' : e}
    
    revision_ids = []
    response_string = ''
    for i in resp :
        response_string = response_string + i
    root = ET.fromstring(response_string)
    for i in root.findall(xmlns+'page/'+xmlns+'revision/'+xmlns+'id') :
        revision_ids.append(i.text)
    return {'id': revision_ids, 'error' : 0}
    