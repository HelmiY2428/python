import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db1 = client1["db_test"]
cl1 = db1["mahasiswa"]

doc1 = [
    {"_id": 191410001, "nama":"aa herdi"},
    {"_id": 191410002, "nama":"alan agus"},
    {"_id": 191410003, "nama":"aditya nur"},
    {"_id": 191410004, "nama":"deni priyadi"},
    {"_id": 191410005, "nama":"gerald"}
]

data1 = cl1.insert_many(doc1)