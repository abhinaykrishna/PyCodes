# Creating Connection
from pymongo import MongoClient
conn = MongoClient('mongodb://localhost:27017/')

# Display All Dbs
db_list = conn.list_database_names()
print(db_list)

# Selecting a DB - use db (If the database exists, the database will be returned else, a database will be created.)
db = conn['myDB']

# show collections
col_list = db.list_collection_names()
print(col_list)

# Selecting a Collection
col = db['student']

# Inserting Data
document = {'Name': 'John', 'Regd_id': '1', 'Age': 20, 'Sex': 'M'}
returnval = col.insert_one(document)
print(returnval.inserted_id)
# insert_one returns a Result object. Using the attribute inserted_id, we can retrieve the insertion id.

document_list = [
    {'Name': 'Kelley', 'Regd_id': '2', 'Age': 21, 'Sex': 'M'},
    {'Name': 'Hannah', 'Regd_id': '3', 'Age': 18, 'Sex': 'F'},
    {'Name': 'Ravi', 'Regd_id': '4', 'Age': 22, 'Sex': 'M'},
    {'Name': 'Rachel', 'Regd_id': '5', 'Age': 26, 'Sex': 'F'},
    {'Name': 'Esther', 'Regd_id': '6', 'Age': 19, 'Sex': 'F'}
]
returnvalue = col.insert_many(document_list)
print(returnvalue.inserted_ids)

# Fetching the first document
print('Find One:')
doc = col.find_one()
print(doc)

# Fetching all the documents
print('Find All')
doc_cursor = col.find()
for doc in doc_cursor:
    print(doc)

# Filter data based on condition
print("Printing based on Filter")
curs = col.find({'Sex': 'F'})
for doc in curs:
    print(doc)

# Filter based on operators
# $eq      Equal to
# $ne      Not Equal
# $gt      Greater than
# $gte     Greater than or Equal
# $lt      Less than
# $lte     Less than or Equal
print("Printing based on Filter Operators")
curs_op = col.find({'Age': {'$gt': 21}})
for row in curs_op:
    print(row)

# $regex to filter documents based on regular expressions.
print("Filter - Regular Expressions")
curs_reg = col.find({'Name': {'$regex': '^R'}})
for row in curs_reg:
    print(row)

# Projection is a technique to restrict the fields/columns in the output.
# We need to pass the dictionary of column names as keys and their project value as 0 or 1, where 1 projects it in the output and 0 hides it from the output.
# By default, _id will be displayed in the output. So, we need to explicitly specify its value to be zero if we do not want to project _id in the output.
curs_pro = col.find({}, {'_id': 0, 'Name': 1, 'Age': 1})
for row in curs_pro:
    print(row)

# To sort the result set, we use the sort() method of cursor class whose syntax is as shown below.
# collection_obj.find({}).sort(Key,Order)
# Where, key is a mandatory argument which is used to specify the field on which we need to sort.
# And, order is an optional argument which is used to specify the sort order. If you do not specify the sort order, by default ascending order sort will take place. For Descending order, we need to pass -1  whereas 1 is for ascending order.
curs_sort = col.find({}).sort('Age', 1)
for row in curs_sort:
    print(row)


# To limit the number of documents to be displayed, we use limit() method of cursor class.
# We need to pass the number of documents to be displayed as an argument to limit() method.
curs_limit = col.find({}, {'_id': 0, 'Name': 1, 'Age': 1, 'Sex': 1}).limit(2)
for row in curs_limit:
    print(row)


# To delete documents from the collection, we use delete_one() and delete_many() methods of collection class.
# delete_one():   delete_one method deletes the first document that matches with the given query.
# delete_many():  delete_many() method deletes all the document that matches with the given query.
# *** If not provided with a query, delete_one will delete the first document from the collection where as delete_many will delete all the documents.
# *** Delete_many will return a delete object.
# *** Delete object has an attribute deleted_count which holds the number of records deleted.

col.delete_one({'Regd_id': '1'})
col.delete_many({'Regd_id': '2'})
curs_del = col.find({})
for row in curs_del:
    print(row)


# To update documents, we use update_one() and update_many() methods of collection class.
# update_one():   update_one method updates the first document that matches with the given query.
# update_many():  update_many() method updates all the document that matches with the given query.
# First Argument for the update method is query and second argument is the update dictionary whose key is ‘$set’ and its value is a dictionary which specifies the fields to be updated
# *** If not provided with a query(first argument as empty), update_one will update the first document from the collection where as update_many will update all the documents.
# update_many will return a update object.
# update object has an attribute modified_count which holds the number of records updated.

col.update_one({'Regd_id': '3'}, {'$set': {'Age': 25}})
col.update_many({'Regd_id': {'$gt': '4'}}, {'$set': {'Age': 30}})
curs_find = col.find({}, {'_id': 0, 'Regd_id': 1, 'Age': 1})
for row in curs_find:
    print(row)

# Count the Rows
print(col.find().count())

# To Drop a Collection
col.drop()
for doc in col.find():
    print(doc)


