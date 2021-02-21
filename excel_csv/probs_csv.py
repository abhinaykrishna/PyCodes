# 1. Write a Python program to write the following data into persons.csv
# ID,NAME,AGE,SEX
# 1,James,20,M
# 2,Katey,10,F
# 3,Kiran,40,M
# 4,Radha,19,F

import csv
with open (r'persons.csv','w') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['ID','Name','Age','Sex'])
  writer.writerow([1,'James',22,'M'])
  writer.writerow([2,'Katey',10,'F'])
  writer.writerow([3,'Kiran',40,'M'])
  writer.writerow([4,'Radha',17,'F'])

# 2. Write a Python program to display all the females from persons.csv

with open(r'persons.csv','r') as csvfile1:
  reader = csv.reader(csvfile1)
  print("Female Employees")
  for row in reader:
    if row[3] == 'F':
      print(row)

# 3. Write a Python program to display all the minors from persons.csv
with open(r'persons.csv','r') as csvfile2:
  readers = csv.reader(csvfile2)
  print(type(reader))
  print('Minors')
  my_list = []
  for row in readers:
    my_list.append(row)

  for row2 in my_list[1:]:
    if int(row2[2]) <= 18:
      print(row2)

  header = ['3:santosh:23']

  print(len(header[1:]))