import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Admin:Admin404@cluster0.t5ugo.mongodb.net/")

# Create a database and collection
mydb = myclient['project1']
mycol = mydb['Students']

dict1 = [{"name": "Manantsoa", "age": 25},
         {"name": "Claudino", "age": 43},
         {"name": "Alex", "age": 32},
         {"name": "Kevin", "age": 12}]

# Insert multiple documents
x = mycol.insert_many(dict1)

s = mycol.find()

print(x.inserted_ids)

# Print all documents in the collection
for i in s:
    print(i)