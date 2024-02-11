import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["db_test"]
cl = db["mahasiswa"]

for x in cl.find({"_id": 191410004}, {"_id": 0}):
    print(x)

