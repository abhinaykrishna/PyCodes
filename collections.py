# Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences.
# Sample Input  -  Sample Output
# [1,1,5,100,-20,-20,6,0,0] -  3
# [10,20,30,40,30,20] - 0
# [1,2,2,3,4,4,4,10]  -  3

def list_adjacent_postiion_check(array):
  count = 0
  for i in range(len(array)-1):
    if array[i] == array[i+1]:
      count+=1
  print('No. of Adjacent Positions are - ',count)
list_adjacent_postiion_check([1,1,5,100,-20,-20,6,0,0])

# Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
# The ticket number should be generated as airline:src:dest:number where
# Consider AL1 as the value for airline
# src and dest should be the first three characters of the source and destination cities.
# number should be auto-generated starting from 101
# The program should return the list of ticket numbers of last five passengers.
# Note: If passenger count is less than 5, return the list of all generated ticket numbers.


def ticket_generator(airline,count,src,dest):
  tickets = []
  for i in range(count):
    tickets.append(airline+ ":" +src[:3]+ ":" +dest[:3]+ ":" +str(101+i))
  if count > 5 :
    return tickets[-5:]
  else:
    return tickets

print(ticket_generator("AI",6,"Bangalore","London"))

# Write a Python function proper_divisors(num) which returns a list of all the proper divisors of given number.
# Example: Proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110

def proper_divisors(num):
  result = []
  for i in range(1,int(num/2)+1):
    if num % i == 0:
      result.append(i)
  return result 

print(proper_divisors(220))


# Write a Python function generate_fibanacci(n) to return a list of first n Fibonacci numbers.

def generate_fibanacci(n):
  my_list = [0,1]
  for i in range(3,n+1):
    my_list.append(my_list[-1]+my_list[-2])

  return my_list

print(generate_fibanacci(10))

# Write a Python program to generate the next 15 leap years starting from a given year. Populate the leap years into a list and display the list.

def check_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False 

def leap_gen(year):
  result = []
  if check_leap(year):
    result = [year]
    for i in range(15):
      result.append(result[-1]+4)
    return result
  else:
    for i in range(1,4):
      if check_leap(year+i):
        found_nearest = year+i 
    result = [found_nearest]
    for i in range(15):
      result.append(result[-1]+4)
    return result  
    
print(leap_gen(2016))
print(leap_gen(1993))

# Given a string containing uppercase characters (A-Z), compress the string using Run Length encoding. Repetition of character has to be replaced by storing the length of that run.
# Write a python function encode(message)  which performs the run length encoding for a given String and returns the run length encoded String.
# Provide different String values and test your program.
# Example: message=AAAABBBBCCCCCCCC  output: 4A4B8C

# Approach 1 - using OrderedDict

from collections import OrderedDict 
def runLengthEncoding(input): 
  
    # Generate ordered dictionary of all lower 
    # case alphabets, its output will be  
    # dict = {'w':0, 'a':0, 'd':0, 'e':0, 'x':0} 
    
    dict=OrderedDict.fromkeys(input, 0) 
  
    # Now iterate through input string to calculate  
    # frequency of each character, its output will be  
    # dict = {'w':4,'a':3,'d':1,'e':1,'x':6} 
    
    for ch in input: 
        dict[ch] += 1
  
    # now iterate through dictionary to make  
    # output string from (key,value) pairs 
    output = '' 
    
    for key,value in dict.items(): 
         output = output + key + str(value) 
    return output 

input="wwwwaaadexxxxxx"
print(runLengthEncoding(input)) 
   
# Approach 2 - 

def encoded(message):
    output=''
    previous=message[0]
    i=1
    count=1
    while len(message)>i:
        if previous==message[i]:
            count+=1
        else:
            output+=str(count)+previous
            count=1
            previous=message[i]

        if i==len(message)-1:
            output += str(count) + previous
        i+=1
    if len(message)==1:
        output += str(count) + previous
    return output

print(encoded(input))

# Represent a small bilingual (English-Swedish) glossary given below as a Python dictionary
# {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
# and use it to translate your Christmas wishes from English into Swedish.
# That is, write a python function translate(b_dict,list_words) that accepts the bilingual dictionary and a list of English words (your Christmas wish) and returns a list of equivalent Swedish words. 

# Approach 1 - Searching 

def translate(b_dict,list_words):
  output = ''
  for i in list_words:
    if i in b_dict.keys():
      output+=b_dict[i]+" "
  print(output)

translate({"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} , ["christmas","new","and"])

# Approach 2 -  using Lists

def translate(b_dict,list_words):
  output = [ ]
  for i in list_words:
    output.append(b_dict[i])
  return output

translate({"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} , ["christmas","new","and"])

# Split String and Join String based on delimeter as space

sample_string = "Abhinay's Macbook Air"

def split_string(str):
  # Split the string based on space delimiter 
  list_string = str.split(' ')
  return list_string

split_string(sample_string)

# ["Abhinay's", 'Macbook', 'Air']

def join_string(str):
  # Join the string based on '-' delimiter
  string = '-'.join(str)
  return string

join_string(sample_string)


# A-b-h-i-n-a-y-'-s- -M-a-c-b-o-o-k- -A-i-r