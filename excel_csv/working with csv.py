import csv

# There is a module named csv which is used to handle CSV files. It consists of methods for read and write operations.
# In order to open a CSV file we use open() method. This method accepts two mandatory arguments which are the filename and the mode.
# They are three different modes:
# Read mode - 'r' is used to open a file in read mode.
# Write mode - 'w' is used to open a file in write mode.
# Append mode - 'a' is used to open a file in append mode.
# Note: Whenever you try to open a file which is not existing on the file system, a new file will be created by the open method. The difference between write mode and append mode is 'In write mode, the existing contents of the files will be deleted whereas in append mode the existing contents will be retained'.


# Methods in CSV Module

# Read Methods
#---------------
# reader() - reader  method accepts file object as an argument and returns a reader object. We can read each record as a list where each element in the list represents a column value.

with open (r'excel_csv/data.csv','r') as csvfile:
  reader = csv.reader(csvfile)
  for record in reader:
    print(record)

# DictReader() - DictReader() accepts file object as an argument and returns a DictReader object. Each record of csv file will be fetched as dictionary where keys represent the column names and values are their corresponding values.

with open (r'excel_csv/data.csv','r') as csvfile1:
  reader = csv.DictReader(csvfile1)
  for record in reader:
    print(record)

# Write Methods
#---------------
# writer() - writer method accepts file object as an argument and returns a csv writer object. We need to use writerow method in order to insert records. Lists are used to insert the data into file.

with open(r'excel_csv/data.csv','w') as csvfile2:
  writer=csv.writer(csvfile2)
  writer.writerow(['EmpId','Emp Name','Salary'])
  writer.writerow([1,'Ramesh',22001.00])
  writer.writerow([2,'Rakesh',26501.00])
  writer.writerow([3,'Raju',27789.00])
# If you observe, we get a blank line between every record. This is because writerow inserts a newline after every insertion and also open method also inserts a newline character. It can be removed as follows:

# *** with open(r'excel_csv/data.csv','w',newline='')) as csvfile:

# DictWriter() - DictWriter accepts filename and field names as arguments. Data which needs to be inserted should be in dictionary format and the keys of dictionary should match with the field names.

with open(r'excel_csv/data.csv','w',newline='') as csvfile3:
    fields=['EmpId','Emp Name','Salary']
    writer=csv.DictWriter(csvfile3,fields)
    writer.writeheader()
    writer.writerow({'EmpId':1,'Emp Name':'Ramesh','Salary':22001.00})
    writer.writerow({'EmpId':2,'Emp Name':'Rakesh','Salary':26501.00})
   


