General Notes:
- Django allows for html code to be dynamically updated as user interacts with website
- Django allows developer to code python functions into http responses
- Django best practice is to preface index.html files with the app name (ie hello/index.html) to avoid having conflicting index file names
- Django is very powerful for storing data inside of web-based databases


Django commands:
- pip3 install Django
- HTTP: protocal for how messages are sent back and forth over the internet
    - HttpResponse("some string"): imported django functionality to give an http response
    - from django.http import HttpResponse


Steps to generating django app:
1) django-admin startproject <PROJECT_NAME>: automatically creates starter files to build web application (ex: Lecutre 3)
    - project is where a developer can build multiple apps within (think google)
2) python manage.py 
    - runserver: command to run manage.py and start up web application
    - startapp <app_name>: command to create an application (think google maps) (ex: hello)
3) settings.py:
    - add new app to list of apps to run (INSTALLED_APPS = ['app_name'])
4) views.py: things a user might want to see
    - add function definition to say what to do when user interacts with url
    - def index(request):
        return HttpResponse("response")
5) urls.py: file to define which urls are available to interact with for that app
    a) create urls.py in app directory
    b) add: from django.urls import path
    c) add: from . import views ("." means from current directory)
    d) add urls to list variable "urlpatterns"
        - paths("", views.index, name="index")
        - "" says when user visits the default route
        - views says run function from views.py
        - index is name of function to call when visiting url from views.py
        - name makes path easy to reference
    e) go to urls.py in overall project directory and add path to new application
        - and include all urls from urls.py in application
        - path('hello/', include("hello.urls")): look at urls.py inside of hello directory to see additional urls user can access
        - make sure to import "path" at top from django.urls


Adding additional functionality:
- add additional funciton to views.py
- add a new path in urls.py so if user adds additional pathway (ie: /hello/Brian/) then it will run new function
- add in additional parameter to function definition to parameterize function
        - use formatted string to use placeholder for output in HttpResponse
        - use <str:name> as first path parameter to pass user input from url into new function
        
        
To create html code more robustly:
- return render(request, "hello/index.html") in views.py index function definition
        - from django.shortcut import render
- pass name of html template as arguement
- create new directories for "template" sub-folder "hello" in larger "hello" app directory
- render can take a 3rd arguement called the context
        - context is all of the variables we want template to have access to
        - passed as a dictionary of key:value pairs
        - Django specicifc syntax to interact with html template:
                - use {{variable}} to plug in value of variable in this location within template
                - use {% logic statement %} to enter conditional statement in html template (see newyear/index.html)
                        - can do the same thing to loop through a "for" statement (see tasks/index.html)
                        - can also provide an {% empty %} condition to tell html what to display if loop is empty
- template inheritance:
        - ability to define general layout and apply it to multiple html pages using Django (layout.html)
        - contains basic layout common to all pages
        - {% block body %} and {% endblock %} to denote what changes between html pages
        - extend layout html page within each individual html file and add changing code within block
- linking urls:
        - reference NAME of url in html href rather than full url path to avoid repitition
                - generally bad practice to hardcode urls
        - to avoid namespace collision (two urls with same name), add app_name to urls.py
                - use "{% url 'app_name:url_name' %}" to target app-specific url name
        
        
Adding static style css files:        
- create a new directory "static" and populate with css files
- add command {% load static %} to top of html template
        - link stylesheet but in link include href="{% static 'newyear/syles.css' %}"
        
        
Python functions:
- datetime:
        - import datetime
        - now = datetime.datetime.now() to have access to now.year, now.month, now.day, ect.
      
      
HTML Forms:
- action: use url to send form input back to a different url
- methods:
        - Get: implicit, used to request a particular page
        - Post: used to change the state of a particular page
- Django can create forms for us:
        - "from django import forms"
        - provides automatic form generation that can take multiple different inputs
        - also automatically provides "client side validation" which provides feedback to user on whether input is valid or not
                - server is not getting any of this data, feedback is all done on the webpage
        - want to include both client side AND server side validation of user input
                - if on older version of webpage, server may have more up-to-date logic on valid user entry
        - use return HttpResponseRedirect() to redirect user to new page after submitting a form


Designing for Site Security:
- CSRF verification failed: "Cross Site Request Forgery", security vulnerability Django recognizes if site is not designed in a secure way
- to avoid this, add in hidden CSRF token:
        - adds in unique token each time user accesses site that is submitted with form, to ensure no forgery is committed
- django has this by default (Middleware in settings.py)
        - add into html page within django notation {% csrf_token %}
        
        
Sessions:
- django can remember who a specific user is and stores data about a particular session (ie: user ID)
- instead of global task variable which is the same for all users, store task variable inside user's session
- by default, django stores this info inside of a table, will throw an error if one is not created
        - must run in terminal: python manage.py migrate

