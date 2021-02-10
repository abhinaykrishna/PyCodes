# Write a Python function factorial(num) which returns the factorial of a given number.

def factorial(num):
  result = 1
  for i in range(2,num+1):
    result *= i

  return result

print(factorial(10))

# Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false. Invoke the function and based on return value print the output.

# Negative Slicing and Type Convert Approach
def is_palindrome(num):
  convert = str(num)
  reverse = convert[::-1]
  if num == int(reverse):
    print(num,'is a palindrome')
  else:
    print(num,'not a palindrome')
  
is_palindrome(666)

# Mathematical Approach
def is_palindrome2(num):
  reverse_number = 0
  while(num > 0):
    last_digit = num % 10 
    reverse_number = reverse_number * 10 + last_digit
    num //= 10
  if num == reverse_number:
     print("The number is palindrome!")
  else:
    print("Not a palindrome!")

is_palindrome2(552)

# Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false. Invoke the function and based on return value print the numbers are amicable numbers or not.
# num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of num1 is equal to num2 and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.
# Example: 220 and 284 are amicable numbers as
# Proper devisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 whose sum is 284
# Proper devisors of 284 are 1, 2, 4, 71, 142 whose sum is 220

def check_amicable_numbers(num1, num2):
  sum_of_num1 , sum_of_num2 , half_num1, half_num2 = 0 , 0 , int(num1/2) , int(num2/2)
  for i in range(1,half_num1 + 1):
    if num1 % i == 0:
      sum_of_num1+=i
  for j in range(1,half_num2 + 1):
    if num2 % j == 0:
      sum_of_num2+=j
  
  print(sum_of_num1,sum_of_num2,sep=' - ')

  if sum_of_num1 == num2 and sum_of_num2 == num1:
    print('{} & {} are amicable'.format(num1,num2))
  else:
    print('{} & {} are not amicable'.format(num1,num2))

check_amicable_numbers(284,220)


# Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and returns value of the integer num rotated to the right by n positions. Assume both the numbers are unsigned. Invoke the function and print the return value.
# Hint: use >> binary operator to shift the bits.
# Example: num=60, n=2 result=15

def right_shift(num,n):
  print(num >> n)

right_shift(60,2)

# Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True if the number is strong number else false. Invoke the function and based on return value print the number is strong number or not.
# A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.
# Example:145 is strong number as
# 1!=1
# 4!=24
# 5!=120
# Sum of all these is 145

def check_strong_number(num):
  result , check = 0 , num
  while(num > 0):
    digit = num % 10
    result += factorial(digit)
    num = num // 10

  if result == check :
    print("strong number")
  else:
    print("not a strong number")

check_strong_number(145)