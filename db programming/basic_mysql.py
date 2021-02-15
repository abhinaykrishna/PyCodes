import mysql.connector
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
parameter="100"
query="DELETE FROM Computer WHERE CompId="+parameter
cur.execute(query)
print(cur.rowcount)
cur.close()
con.commit();
con.close()
# The cursor object has a rowcount attribute which is used to get the number of rows affected by the last query.


# Exception Handling
# ------------------------------------------

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
try:
    cur.execute("INSERT INTO Computer_1 VALUES (100)")
    con.commit()
except mysql.connector.ProgrammingError as e:
    print(e)
finally:
    con.close()
# The above code has an error in the query. The output of the print statement is 1146 (42S02): Table 'yourdatabase.computer_1' doesn't exist. It is always a good practice to close connections in the finally block.

# NameError - Trying to perform a cursor operation without creating it.

# ProgrammingError - Trying to perform cursor operation after cursor being closed.

# OperationalError - MySQL connection not available. (Trying to perform operations after connection is closed)


# Processing the result of a SELECT query
# ------------------------------------------

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
cur.execute("SELECT * FROM Computer")
for row in cur:
    print(row)
cur.close()
con.close()

# Processing the result of a select query is different from the other DML statements. While execution, DML statements return number of rows affected, executing a select query returns the rows fetched by the query.

# The return value of a select query is a list of rows and we can iterate row by row. Each row is represented as a tuple.

# The column values retrieved from the query are converted from the MySQL data types to their equivalent Python datatypes. For example, Varchar2 is converted automatically to string in Python.

# FETCH
# ------------------------------------------

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
cur.execute("SELECT * FROM Computer")
print(cur.fetchone())
print(cur.fetchall())
print(cur.fetchmany())
print(cur.fetchmany(2))
cur.close()
con.close()

# Data from the result set of a select query can be retrieved using the fetch methods of cursor object. There are three fetch methods, 

# fetchone - used to fetch one record from the result set

# fetchall - used to fetch all the records from the result set

# fetchmany -  used to fetch multiple records from the database. fetchmany accepets a default parameter number. When passed, the mehtod will fetch give number of record. Else, it will fetch only one record

# Extract data
# ------------------------------------------

# Like SELECT * FROM Computer
# Like SELECT Make,CompId FROM Computer

# We can extract the individual columns from the row tuple in two ways:

# In the first way, individual variable names are used for each value in the tuple:
cur.execute("SELECT * FROM Computer")
for column1,column2,column3,column4 in cur:
    print(column3,column1)

# In the second way the entire tuple is stored in a single Python variable:
cur.execute("SELECT * FROM Computer")
for row in cur:
    print(row[2],row[0])
# We can access individual columns by using the index position, which starts with zero.

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
cur.execute("SELECT sum(Salary) AS sum FROM Employee")
for row in cur:
    print(row[0])
cur.close()
con.commit()
con.close()

# In the above code, we are using an alias, but in the Python code, we are just interested in the value of the column and not the column name itself.

# Performance Issues --- Bind Variables Queries
# ------------------------------------------

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
list_of_Id=[100,102,103,104]
for id in list_of_Id:
    cur.execute("SELECT * FROM Computer WHERE CompId="+str(id)) 
    for CompId,Make,Mdel,MYear in cur:
        print(Make,CompId)
cur.close()
con.close()
# The problem with this approach is the query will be compiled by MySQL every time in the loop. If the loop runs 1000 times, then the query will be compiled by Oracle 1000 times leading to performance issues.

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
list_of_Id=[100,102,103,104]
for id in list_of_Id:
    cur.execute("SELECT * FROM Computer WHERE CompId=%(c_id)s",{"c_id":id})
    for CompId,Make,Model,MYear in cur:
        print(Make,CompId)
cur.close()
con.close()

# The mapping between the bind variables and Python variables are supplied through a dictionary. This dictionary has key as the bind variable and the corresponding value as the Python variable. The value of Python variable/value is substituted in MySQL bind variable and is then sent to MySQL.

# Multiple Operations
# ------------------------------------------

import mysql.connector
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
cur.execute("SELECT CompId,MYear from Computer where Make='Dell'")
for CompId,MYear in cur:
    new_year=int(MYear)+1
    cur2=con.cursor()
    cur2.execute("UPDATE Computer SET MYear=%(year)s WHERE CompId=%(c_id)s",{"year":new_year,"c_id":CompId})
cur.close()
con.commit()
con.close()

# Stored Functions
# ------------------------------------------

# Stored functions that are stored in the Database can also be invoked using execute method of cursor. The required arguments can be passed by argument binding during the function call. The below is the Function definition

# DELIMITER //
# CREATE FUNCTION Increase_by_100 (NUMBER INT) RETURNS INT
# BEGIN
# RETURN NUMBER+100;
# END
# //

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
cur.execute('SELECT INCREASE_BY_100(%s)',[10])
print(cur.fetchone())

# To Invoke a Stored Procedure, the callproc method of cursor should be used. The arguments that are needed needs to be passed as a list in the second argument. This method will return another list similar to argument list which contains the changes to the OUT/INOUT arguments passed.

# CREATE PROCEDURE promotion_discount(IN DISCOUNT INT, INOUT PRICE INT)
# BEGIN
# SET PRICE=PRICE*(1-DISCOUNT/100);
# END

import mysql.connector 
con = mysql.connector.connect(host="host",user="username",passwd="password",database="database")
cur = con.cursor()
args=[10,1000]
res=cur.callproc('promotion_discount',args)
print(res)
