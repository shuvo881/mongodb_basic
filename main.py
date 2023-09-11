import pymongo
import connection


def create_database(database_name):
    my_client = connection.create_connection()
    mydb = my_client[database_name]
    return mydb


def create_table(database, table_name):
    table = database[table_name]
    return table


def insert_table(table, data):
    if len(data) > 1:
        records = table.insert_many(data)
        return records
    record = table.insert_one(data[0])
    return record


# creating databases
teach_db = create_database('teacher')
stu_db = create_database('student')

# create table
teach_details_table = create_table(teach_db, 'teacher details')
stu_details_table = create_table(stu_db, 'student details')

# insert into database
stu1 = [{
    'name': 'shuvo',
    'class': 9
}]

"""row = insert_table(stu_details_table, stu1)
print('Student Id: ', row.inserted_id)"""


teachers = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]

"""rows = insert_table(teach_details_table, teachers)
print("Teachers ID: ", rows.inserted_ids)"""

myquery = { "address": { "$gt": "A" } }
x = teach_details_table.find(myquery).sort('name', -1)

for y in x:
    print(y)


myquery = { "address": "Mountain 21" }

teach_details_table.delete_one(myquery)


myquery = { "address": {"$regex": "^S"} }

x = teach_details_table.delete_many(myquery)

print(x.deleted_count, " documents deleted.")