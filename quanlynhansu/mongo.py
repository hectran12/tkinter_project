import pymongo

url = ''
collection = ''

def conn():
    global url, collection
    # connection
    client = pymongo.MongoClient(url)

    # check database
    list_database = client.list_database_names()
    
    if "quanlynhanvien" not in list_database:
        # create database
        db = client["quanlynhanvien"]
        # create collection
        collection = db["nhanvien"]

        # insert
        data = {
            "name": "Nguyen Van A",
            "age": 20,
            "address": "Ha Noi"
        }
        collection.insert_one(data)

        # remove
        collection.delete_one(data)
        print("Thiệp lập thành công database")
    else:
        # get database
        db = client["quanlynhanvien"]
        # get collection
        collection = db["nhanvien"]

        print("Kết nối thành công database")


def getAll():
    global collection
    # get all data
    data = collection.find()
    return data


def add(name, age, address):
    global collection
    # insert
    # get count
    count = collection.count_documents({})
    data = {
        "id": count+1,
        "name": name,
        "age": age,
        "address": address
    }
    collection.insert_one(data)


def delete(id):
    global collection
    # delete
    collection.delete_one({"id": id})


def update(id, name, age, address):
    global collection
    # update
    # remove old data
    delete(id)
    # add new data
    data = {
        "id": id,
        "name": name,
        "age": age,
        "address": address
    }
    collection.insert_one(data)
    
    

