# In the Athlete class given below,
# a. make all the attributes private and
# b. add the necessary accessor and mutator methods
# Represent Maria, the runner and make her run.
# class Athlete:
#     def __init__(self,name,gender):
#         self.name=name
#         self.gender=gender
#     def running(self):
#         if(self.gender=="girl"):
#             print("150mtr running")
#         else:
#             print("200mtr running")

class Athlete:
  def __init__(self, name, gender):
    self.__name = name
    self.__gender = gender

  def running(self):
    if (self.__gender == "girl"):
      print("150mtr running")
    else:
      print("200mtr running")

  def get_name(self):
    return self.__name

  def set_name(self,value):
    self.__name = value

  def get_gender(self):
    return self.__gender

  def set_gender(self,val):
    self.__gender = val

R1 = Athlete("Maria","girl")
R1.running()

# A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
# A student is identified by student id, age and marks in qualifying exam. Data are valid, if:
#   a. Age is greater than 20
#   b. Marks is between 0 and 100 (both inclusive)
# A student qualifies for admission, if
#   a. Age and marks are valid and
#   b. Marks is 65 or more
# Write a python program to represent the students seeking admission in the university.
# Continuing with the previous scenario, a student eligible for admission has to choose a course and pay the fees for it. If they have scored more than 85 marks in qualifying exam, they get 25% discount on fees.
# Valid course ids and fees are given below: 
# 1001 - 25575, 1002 - 15500
# Extend the program written in the previous assignment to include the above requirement.

class Student:
  
  def __init__(self,student_id,marks,age):
    self.__student_id = student_id
    self.__marks = marks    
    self.__age = age
    self.__course_id = None 
    self.__fees = None

  def validate_marks(self):
    if self.__marks >= 0 and self.__marks <= 100:
      return True
    else:
      return False

  def validate_age(self):
    if self.__age > 20:
      return True
    else:
      return False

  def check_qualification(self):
    if Student.validate_marks(self) and Student.validate_age(self):
      if self.__marks >= 65:
        return True
      else:
        return False
    else:
      return False

  def set_student_id(self,val):
    self.__student_id = val

  def set_marks(self,val):
    self.__marks = val

  def set_age(self,val):
    self.__age = val

  def set_course_id(self,val):
    self.__course_id = val

  def set_fees(self,val):
    self.__fees = val

  def get_student_id(self):
    return self.__student_id

  def get_marks(self):
    return self.__marks

  def get_age(self):
    return self.__age

  def get_course_id(self):
    return self.__course_id

  def get_fees(self):
    return self.__fees

  def choose_course(self,course_id):
    if course_id == 1001 or course_id == 1002 :
      if course_id == 1001:
        self.set_course_id(1001)
        self.set_fees(25575)
      else:
        self.set_course_id(1002)
        self.set_fees(15500)
      
      if self.__marks > 85:
        fees_discount = 0.75 * self.get_fees()
        self.set_fees(fees_discount)
      return True

    else:
      return False


s1 = Student(101,91,24,)
s2 = Student(102,64,21)
s3 = Student(104,80,19)

print(s3.check_qualification())

s3.__age = 21
print(s3.check_qualification())

s3.set_age(21)
print(s3.check_qualification())
print(s3.get_age())

s1.fees()

if s1.check_qualification():
  print("Student Qualified")
  if s1.choose_course(1002):
    print(s1.get_course_id(), s1.get_fees())
  else:
    print("Course is not valid or Student marks are less than 85")
else:
  print("Student is not Qualified")