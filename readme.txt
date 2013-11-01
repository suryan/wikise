

1. Prerequisites
Python libraries  :
  1. Django
  2. uwsgi (Optional. For scaling)
  3. Requests
  
--------------------------------------------------------------------------------------------------------------------------------
start webserver  with command 

> python wikise_server.py

1. localhost: http://localhost:8000
2. Json response http://localhost:8000/info/?article=<article name>
  Example: http://localhost:8000/info/?article=eclipse

----------------------|  
Change Log            | 
----------------------|  

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

