# Zip Zap Zoom

def Excersise(number):
	if number % 3 == 0 and number % 5 == 0:
		print('Zoom')
	elif number % 3 == 0:
		print('Zip')
	elif number % 5 == 0:
		print('Zap')
	else:
		print('Invalid')

Excersise(15)

# Sum of number 123 will be 6

def print_sum(number):
	result = 0
	while number > 0:
		remainder = number % 10
		result += remainder
		number = number // 10
	print(result)

print_sum(12345)

# Write a Python program to check whether the given year is leap year or not.

def check_leap_year(year):
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print(year, ' Leap Year')
			else:
				print(year, ' Not a Leap Year')
		else:
			print(year, ' Leap Year')
	else:
		print(year, ' Not a Leap Year')

check_leap_year(1992)

# Write a Python program to find and display the maximum of three given numbers.

def max_of_number(a, b, c):
	if a > b and a > c:
		print(a, " is the greatest")
	elif b > a and b > c:
		print(b, " is the greatest")
	else:
		print(c, " is the greatest")


max_of_number(5, 22, 18)

# Write a Python program to check the given number is prime number or not.

def check_prime(number):
	if number == 2:
		print("PRIME , 2 is the only even prime")
	else:
		for i in range(2, number):
			if number % i == 0:
				print("Print Not PRIME")
				break
		print("PRIME")

check_prime(17)

# Write a Python program to print first n Fibonacci numbers.
# 0 + 1 + 1 + 2 + 3 + 5 + 8 ....

prompt = int(input("1 - List Approach ; 2 - Iterative Approach 2 "))

def Fibonacci(number):
	if prompt == 1:
		store = [0, 1]
		for i in range(3, number + 1):
			store.append(store[-1] + store[-2])
		print(store)
	elif prompt == 2:
		n1, n2, count = 0, 1, 0
		while count < number:
			print(n1)
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count += 1
	else:
		print('Invalid Response - Choose 1 or 2')

Fibonacci(8)

def salary_hike(job_level, salary):
	if job_level == 3:
		updated_salary = salary * 1.15
		print(updated_salary)
	elif job_level == 4:
		updated_salary = salary * 1.07
		print(updated_salary)
	elif job_level == 5:
		updated_salary = salary * 1.05
		print(updated_salary)
	else:
		print(salary)

salary_hike(4, 20000)

# Write a python function, find_square() that accepts an integer number, n and returns the square of n. Invoke the function and display the square of the number.

def find_square(n):
	return n * n

print(find_square(25))

# Write a python function, find_sum() that accepts an integer, n and returns the sum of first, n numbers. Invoke the function and display the sum of first n numbers.

def find_sum(n):
	result = 0
	for i in range(1, n + 1):
		result += i
	return result

print(find_sum(17))