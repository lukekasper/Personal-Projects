### SQL Lecture Notes

General Notes:
- SQL is a database language designed to interact with database management systems (ex: MySQL, PostgreSQL, SQLite)
- BLOB: large binary data type
- Django uses python code to generate below SQL commands for interacting with database


Interacting with data tables in SQL:
- Assign each column a data type
- Can assign contraints to each column (check, default, not null, primary key, unique, ect)
- Add data via insert command
- Use "select" query to get data from table
  - Can use other boolean or numerical expressions to select data from table (ie: OR, > 500)
  - Can use IN to build a query based on a list of values
  - Can use LIKE "%a%": returns anything with an 'a' in it
- Built-in functions also allow calculations: avg, min, max, count
- UPDATE query can update rows of a table to a new value
- DELETE data based on specified conditions
- Other clauses:
  - LIMIT: limits how many rows are returned from table
  - ORDER BY: returns rows sorted in a specified manner
  - GROUP BY: group flights by a certain value (ie origin = New York)
    - Use HAVING with GROUP BY to add additional constraint (ie must have at least 3 flights leaving from NY to display)
- CREATE INDEX: Add a way to look up a value by one of its parameters


Table Structures
- Foreign Key: way to connect two data tables by use of unique ID
  - One data table references the ID of a second data table to look up information about that ID
- Join table: contains IDs from two seperate tables to inter-relate them
  - Allows many passangers to be related to many flights for example
  - A passanger can be on multiple flights, and a flight can have multiple passangers 
 - Can then use JOIN query to join all tables back together in a readable way
  - Must specify what columns we want and how to relate the two tables (JOIN ... ON ...) (inner join)
  - Other JOINS are available as well (similar to power query or pivot tables in excel)


SQL Injection:
- It is possible to use SQL syntax to comment out other portions of a request or lookup
  - Ie: enter username of "hacker"--" usese -- to comment out request for a password
  - Good practice to escape special characters in SQL code


Race Condition:
- Two commands running in parrallel that may conflict with one another
  - Leads to unpredictable/unreplicable results 
- Can place a lock on database to make sure all computations are complete before allowing interactions with the database


Django Models:
- Models are a way of creating a python class of data that we want django to store inside of a database
- Inside of models.py:
  - One model for each of the main tables we care about
  - Documented on django website is types of fields for data (ie CharField) that can be included in a Django model
    - Type ForeignKey allows user to reference an id from another model
- Migrations:
  1)  create a migration which define changes we want to the database and then
    - python manage.py makemigrations: to create migration
    - Creates migrations file for you
    - Reflects changes made in models.py 
  2)  migrate them to update the db
    - python manage.py migrate: applies migration to database
- Can enter django's shell to run python commands directly on database: pyhton manage.py shell
- Any model (or python class in general) can implement a "__str__" function that returns a string representation of that object
- on_delete=models.CASCADE: applies deletion to downstream references
  - ie) deleting an airport from db would also delete all flights referencing that airport
  - Can be applied to other actions besides on_delete
  - Can also use models.PROTECT to not allow a deletion if there are other references to it
- related_name="departures": can access relation in reverse order
  - If you have an airport, you can get all flights that have that airport as an origin
- Can use views.py to display webages with table data
- <model>.objects.all(): gets all model objects
- <model>.objects.filter(): can get a subset of objects based on specified conditions
- <model>.objects.exclude().all(): does the inverse of filter (excludes all objects under specified conditions)
- Admin app allows direct manipulation of models via Django's built admin interface
  - Must add models in admin.py
  - Can configure models further in order to add customization to the admin interface

More Django:
- Can specify a variable for an html attribute to take as an arguement with: 
  - \<a href="{% url 'flight' flight.id %}"\> (passes variable flight.id into 'flight' url)
- Look up obnject by primary key using: <model>.objects.get(pk=<model_id>)
- HttpResponseRedirect(reverse()): redirects you to a url by passing the name of the url view, rather than the full url pathway
  - Pass an arguement to this view by using args: 
    - HttpResponseRedirect(reverse("flight", args=(flight.id,)))
    - Structured as a tuple!
  
  
Authentication:
- Django has built-in authentication capability
- request.user.is_authenticated: tells if user is signed in or not
- Passing an input as type="password" lets browser know to display password as dots and not text
- Can use django modules to check:
  - from django.contrib.auth import authenticate, login, logout
  - user = authenticate(request, username="", password="")
  - Authentication works as long as user "is not None"
  - Then can use login(request, user)
