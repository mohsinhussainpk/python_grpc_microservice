import pymongo

# #myclient = pymongo.MongoClient("mongodb+srv://admin:FfCOm8WstRX2tKER@cluster0.ek2zd.mongodb.net/pythonGRPC?retryWrites=true&w=majority")
# myclient = pymongo.MongoClient("mongodb+srv://admin:FfCOm8WstRX2tKER@cluster0.ek2zd.mongodb.net/pythonGRPC?retryWrites=true&w=majority")


# mydb = myclient["pythonGRPC"]
# mycol = mydb["Boxes"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)


client = pymongo.MongoClient("mongodb+srv://admin:FfCOm8WstRX2tKER@cluster0.n9amd.mongodb.net/pythonGRPC?retryWrites=true&w=majority")
mydb = client.pythonGRPC
print(mydb)

mycol = mydb["Boxes"]

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)