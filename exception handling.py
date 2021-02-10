# Given a list of numbers, write a Python function to return the list of prime numbers present in it.
# Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]

def list_of_prime(ln):
  result = []
  try:
    for i in ln:
      if i == 2:
        result.append(i)
      else:
        for j in range(2,i):
          if i % j == 0:
            break
        else:
          result.append(i)
  except TypeError:
    print("Incorrect data type passed")
  finally:
    print(result)

list_of_prime([7,9,11,13,15,20,23,2])

# Write a python function find_common_characters(msg1,msg2) to display all the common characters between given two strings. Return -1 if there are no matching characters.
# Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.
# Example: msg1="I like Python", msg2="Java is a very popular language" output=lieyon

def find_common_characters(msg1,msg2):
  s1 = ''.join(msg1.split(" "))
  s2 = ''.join(msg2.split(" "))
  # Can also use replace method - string.replace(" ", "") 
  result = ""
  for i in s1:
    for j in s2:
      if i == j :
        result+=i
        break
    else:
      return -1
  return result

find_common_characters("I like Python","Java is a very popular language")


# Write a python function, find_pairs_of_numbers(num_list,n) which accepts a list of positive integers with no repetitions and returns count of pairs of numbers in the list that adds up to n. The function should return 0, if no such pairs are found in the list.
# Example: num_list=[1, 2, 7, 4, 5, 6, 0, 3], n=6 output:3
# (1 5), (2 4), (6 0)
# num_list= [3, 4, 1, 8, 5, 9, 0, 6], n=9 output:4
# (3 6),(4 5),(1 8),(9 0)

def find_pairs_of_numbers(num_list,n):
  pairs = 0
  my_list = []
  for i in range(len(num_list)-1):
    for j in range(i+1,len(num_list)):
      if num_list[i] + num_list[j] == n:
        pairs+=1
        my_list.append([num_list[i],num_list[j]])

  print("No of Pairs Matched = {}, Pairs are {}".format(pairs,my_list))

find_pairs_of_numbers([1, 2, 7, 4, 5, 6, 0, 3],6)
find_pairs_of_numbers([3, 4, 1, 8, 5, 9, 0, 6],9)


# The python function, find_average() given below, is written to accept a list of marks and return the average marks. On execution, the program is resulting in an error.
# def find_average(mark_list):
#           total=0
#           for i in range(0, len(mark_list)):
#                    total+=mark_list1[i]
#           marks_avg=total/len(mark_list)
#           return marks_avg
# m_list=[1,2,3,4]
# print("Average marks:", find_average(m_list))
# 1: Add code to handle the exception occurring in the code.
# 2: Make the necessary correction in the program to remove the error.
# 3: Make the following changes in the code, execute, observe the results. Add code to handle the errors occurring in each case.
# Case – 1: Initialize m_list as ["1",2,3,4]
# Case – 2: Initialize m_list as given below
# mark1="A"
# mark1=int("A")
# m_list=[mark1,2,3,4]
# Case – 3: Initialize m_list as []
# Case – 4: Make the following change in the for loop statement
# # for i in range(0, len(mark_list)+1):

def find_average(mark_list):
  total=0
  try:
    for i in range(0, len(mark_list)+1):
      total+=mark_list1[i]
    marks_avg=total/len(mark_list)
    return marks_avg
  except IndexError:
    print("Index out of range")
  except NameError:
    print("name error - something not defined but used")
  except TypeError:
    print("Incorrect Data Type passed")
  except ValueError:
    print("Value Error")
  except:
    print("Some Error")

try:
  mark1="A"
  mark1=int("A")
  m_list=[mark1,2,3,4]
  print("Average marks:", find_average(m_list))
except ValueError:
  print("ValueError")

# m_list=["1",2,3,4]
# m_list=[1,2,3,4]



