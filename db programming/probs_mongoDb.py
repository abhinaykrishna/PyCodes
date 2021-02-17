from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/')

db = conn['Demo']
col = db['Employee']

# 1. Write a Python program to insert the following data into the collection Employee.

col.insert_many([
    {'EmpID': 1, 'Name': 'Tim', 'Dept': 'ETA', 'Salary': 21990},
    {'EmpID': 2, 'Name': 'John', 'Dept': 'ADM', 'Salary': 22900},
    {'EmpID': 3, 'Name': 'James', 'Dept': 'FIN', 'Salary': 28100},
    {'EmpID': 4, 'Name': 'Robert', 'Dept': 'ETA', 'Salary': 100000},
])

for row in col.find():
    print(row)

# 2. Write a Python program to display the details of employees earning more than 25000.

curs = col.find({'Salary': {'$gt': 25000}})
for row in curs:
    print(row)

# 3. Write a Python program to display the details of the employees whose names start with 'J' or whose dept has 'A'.

cur_regex = col.find({'$or':[{'Name': {'$regex':"^J"}},{'Dept':{'$regex':"A"}}]})
for row in cur_regex:
    print(row)

# 4. Write a Python program to update the dept of John as "DNA".

col.update_one({'Name': 'John'}, {'$set': {'Dept': 'DNA'}})

# 5. Write a Python program to delete the document of Robert.

col.delete_one({'Name': 'John'})


# 6. Write a python program which displays the following menu and seeks the user input up on its execution.
# Add a new employee
# Update salary of an employee
# Remove an employee 
# Display an employee
# Rules: 
# If 1 is selected, take the employee details from the standard input and insert a new document
# If 2 is selected, input the employee id and the lastest salary. Update the corresponding document
# If 3 is selected, input the employee id and delete the corresponding document
# If 4 is selected, input the employee id and display the corresponding document
# For any other input, display all the employee documents
# Note: Display respective error messages wherever needed.


class CRUD_using_Mongo:
    def __init__(self):
        self.__con = None
        self.__db = None
        self.__col = None
        self.connection_setup()

    def get_col(self):
        return self.__col

    def get_con(self):
        return self.__con

    def get_db(self):
        return self.__db

    def connection_setup(self):
        try:
            self.__con = MongoClient('mongodb://localhost:27017/')
            self.__db = self.__con['Organization']
            self.__col = self.__db['Employees']
        except Exception as e:
            print(e)

    def insert(self):
        EmpID = int(input('Enter Employee ID : '))
        Name = input('Enter Name : ')
        Dept = input('Enter Department : ')
        Salary = int(input('Enter Salary : '))

        insert_statement = self.get_col().insert_one(
            {'EmpID': EmpID, 'Name': Name, 'Dept': Dept, 'Salary': Salary})
        print("1 Record Inserted "+str(insert_statement.inserted_id) +
              ", this is the reference id")

    def update(self):
        print("You are updating Salary of an employee")
        emp_id = int(input('Enter Employee ID : '))
        new_salary = int(input("Enter the Salary : "))

        self.get_col().update_one({'EmpID': emp_id}, {
            '$set': {'Salary': new_salary}})
        print("Salary Updated")

    def delete(self):
        emp_id = int(input('Enter Employee ID : '))
        self.get_col().delete_one({'EmpID': emp_id})
        print("Employee ID "+str(emp_id)+" deleted")

    def display(self):
        emp_id = int(input('Enter Employee ID : '))
        result = self.get_col().find_one({'EmpID': emp_id})
        print(result)

    def display_all(self):
        for row in self.get_col().find({}, {'_id': 0, 'EmpID': 1, 'Name': 1, 'Dept': 1, 'Salary': 1}):
            print(row)


c = CRUD_using_Mongo()
c.insert()
c.update()
c.delete()
c.display()
c.display_all()