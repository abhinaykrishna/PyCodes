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
delete_row = 4
query = "DELETE FROM STUDENT WHERE SID="+str(delete_row)
cur.execute(query)
print("rowcount is used to get the number of rows affected by the last query",cur.rowcount)

# Write a python program which displays the following menu and seeks the user input up on its execution.
# Rules: 
# If 1 is selected, take the student details from the standard input and insert a new record
# If 2 is selected, input the student id and the updated details. Update the corresponding record
# If 3 is selected, input the student id and delete the corresponding record
# If 4 is selected, input the student id and display the corresponding record
# For any other input, display all the student records
# Note: Display respective error messages wherever needed.

input_value = int(input("Select a value from the menu\n"
"1 -> Add a new student\n"
"2 -> Update an existing student detail\n"
"3 -> Remove a student\n"
"4 -> Display a student\n"))

def CRUD(value):
  if value == 1:
    print("CRUD - CREATE")
    s_id = int(input("Enter SID : "))
    s_name = input("Enter Student Name : ")
    course = input("Enter Course Name : ")
    marks = int(input("Enter Marks : "))
    cur.execute("INSERT INTO STUDENT VALUES (?,?,?,?)",(s_id,s_name,course,marks))
    print(str(cur.rowcount)+" Row Inserted")
  elif value == 2:
    print("CRUD - Update Marks")
    record = int(input("Enter the SID to be updated : "))
    user_marks = int(input("Enter the Marks to Update : "))
    cur.execute("UPDATE STUDENT SET MARKS=? WHERE SID=?",(user_marks,record))
    print(str(cur.rowcount)+" Row Updated Successfully")
  elif value == 3:
    print("CRUD - Delete")
    record = int(input("Enter the SID to be deleted : "))
    cur.execute("DELETE FROM STUDENT WHERE SID="+str(record))
    print("Deleted {} record, rows effected : {}".format(record,cur.rowcount))
  elif value == 4:
    print("CRUD - READ")

    count = int(input("How Many Records You Would Like To Fetch : "))
  
    record = []
    while(count>0):
      data=int(input("Enter the SID : "))
      record.append(data)
      count-=1

    for id in record:
      cur.execute("SELECT * FROM STUDENT WHERE SID=?",str(id))
      print(cur.fetchall())
  else:
    print("Invalid Option")
    cur.execute("SELECT * FROM STUDENT")
    print(cur.fetchall())

CRUD(input_value)  

cur.close()
conn.commit()
conn.close()