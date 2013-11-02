

1. Prerequisites

Python libraries  :
  1. Django
  2. uwsgi (Optional. For scaling)
  3. Requests
  
------------------------------------------------------------------------
2. Start webserver  with command 

  > python wikise_server.py

  1. localhost: http://localhost:8000  
     Example : http://en.wikipedia.org/wiki/Malkin_Tower 
               on submit returns revision ids 

  2. Json response http://localhost:8000/info/?article=<article name>
     Example: http://localhost:8000/info/?article=eclipse

Alternate webserver (High Performance)
  1. Modfiy file uwsgi.ini with correct directory path .
  2. Starting webserver on UWSGI
    > uwsgi --ini uwsgi.ini

-------------------------|  
3. Change Log            | 
-------------------------|  

Release notes 0.4
-------------------------
1. Added json reponse http://localhost:8000/info/?article=<article name>


Release notes: 0.3
---------------------------
1. Added Wiki article Revisions fetch page
2. Moved Cherrypy webserver to third party 
3. uwsgi config for starting server on uwsgi server   


-------------------
Release notes: 0.2 
----------------------
Cherrypy webserver for better scaling 

Release notes: 0.1 
---------------------
Django Project 



4.  Manifest 

|-- manage.py
|-- readme.txt
|-- test.xml
|-- thirdparty
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- wsgiserver2.py
|   |-- wsgiserver2.pyc
|   `-- wsgiserver3.py
|-- uwsgi.ini
|-- wikise
|   |-- __init__.py
|   |-- __init__.pyc
|   |-- settings.py
|   |-- settings.pyc
|   |-- templates
|   |   |-- index.html
|   |   `-- media
|   |-- urls.py
|   |-- urls.pyc
|   |-- views.py
|   |-- views.pyc
|   |-- wikiapi.py
|   |-- wikiapi.pyc
|   |-- wsgi.py
|   `-- wsgi.pyc
|-- wikise_server.py
|-- wsgiserver.py
`-- wsgiserver.pyc

5. To dos
   1.  unit tests
