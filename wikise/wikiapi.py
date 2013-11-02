'''
Created on 01-Nov-2013

@author: suryan
'''

import requests
import xml.etree.ElementTree as ET

def fetch(article,attribs) :
    ''' Fetch attributes of the article via  POST from 
        http://en.wikipedia.org/w/index.php'''
    
    xmlns = "{http://www.mediawiki.org/xml/export-0.8/}"
    params = {'title' :'Special:Export', 'action' : 'submit',
                  'pages' : article, 'catname' : '', 'wpDownload' : '1'}
    data_paths = { 'id': xmlns+'page/'+xmlns+'revision/'+xmlns+'id',
                  'timestamp': xmlns+'page/'+xmlns+'revision/'+xmlns+'timestamp',
                  'username': xmlns+'page/'+xmlns+'revision/'
                  +xmlns+'contributor/'+ xmlns+'username'}

    try:
        resp = requests.post('http://en.wikipedia.org/w/index.php',
                             params = params)
    except requests.exceptions.RequestException as e:
        return {'error' : str(e)}
    
    data = {}
    response_string = ''
    for i in resp :
        response_string = response_string + i
    root = ET.fromstring(response_string)
    for attrib in attribs :
        data[attrib] = []
        for i in root.findall(data_paths[attrib]) :
            data[attrib].append(i.text)
    return {'result': data, 'error' : 0}
    