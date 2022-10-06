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
- 
