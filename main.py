import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

# Write a python program to create a table student with the below columns

# SID - INT , PRIMARY KEY
# SNAME - VARCHAR2(20)
# COURSE - VARCHAR2(20)
# MARKS - INT

cur.execute("CREATE TABLE STUDENT ( SID INT PRIMARY KEY, SNAME VARCHAR2(20),COURSE VARCHAR2(20),MARKS INT);")

# Write a python program to insert the following data into the student table.

cur.execute("INSERT INTO STUDENT VALUES (1,'THOMAS','PYTHON',82);")
cur.execute("INSERT INTO STUDENT VALUES (2,'Kevin','Java',81);")
cur.execute("INSERT INTO STUDENT VALUES (3,'Adam','Go',90);")
cur.execute("INSERT INTO STUDENT VALUES (4,'John','Python',90);")


# The marks for student 3 are entered wrong. The actual marks were 92. Write a python program to update the marks of student 3.

cur.execute("UPDATE STUDENT SET MARKS=92 WHERE SID=3")

# Write a python program to display all the records of student table.


cur.execute("SELECT * FROM STUDENT")
for row in cur:
  print(row)


# Write a python program to delete the student 4 record of Student table.

cur.execute("DELETE FROM STUDENT WHERE SID=4")

# Write a python program which displays the following menu and seeks the user input up on its execution.
# Rules: 
# If 1 is selected, take the student details from the standard input and insert a new record
# If 2 is selected, input the student id and the updated details. Update the corresponding record
# If 3 is selected, input the student id and delete the corresponding record
# If 4 is selected, input the student id and display the corresponding record
# For any other input, display all the student records
# Note: Display respective error messages wherever needed.

input_value = input("Select a value from the menu\n"
"1 -> Add a new student\n"
"2 -> Update an existing student detail\n"
"3 -> Remove a student\n"
"4 -> Display a student\n")



cur.close()
conn.close()