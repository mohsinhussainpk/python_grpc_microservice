from concurrent import futures
import random
import pymongo
from dotenv import load_dotenv
import os
import grpc

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
print(MONGO_DB_URL)
client = pymongo.MongoClient(MONGO_DB_URL)
mydb = client.pythonGRPC
print(mydb)

mycol = mydb["Boxes"]

mydict = { "name": "box1", "id": 2 , "price": 20, "description": 'description text', "category" :'cat', "quantity": 9 }
#x = mycol.insert_one(mydict)
x = mycol.find_one()
print(x)
print(x['name'])


from db_pb2 import (
    Box,
    GetBoxRequest,
    GetBoxResponse,
    GetAllBoxesRequest,
    GetBoxesResponse,
    CreateBoxRequest,
    CreateBoxResponse,
    UpdateBoxRequest,
    UpdateBoxResponse,
    DeleteBoxRequest,
    DeleteBoxResponse,
    GetBoxesInCategoryRequest,
    GetBoxesInTimeRangeRequest,
    RequestStatus,
)

import db_pb2_grpc


# books_by_category = [Box(name='box1', id=2, price=20, description='disc', category='cat', quantity=9),
# Box(name='box2', id=3, price=20, description='disce', category='cate', quantity=10)
# ]

    # BookCategory.MYSTERY: [
    #     BookRecommendation(id=1, title="The Maltese Falcon"),
    #     BookRecommendation(id=2, title="Murder on the Orient Express"),
    #     BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    # ],


  
  



class DatabaseService(
    db_pb2_grpc.DatabaseServiceServicer
):
    def GetBox(self, request, context):
        x = mycol.find_one()

        box_details = Box(name=x['name'], id=x['id'], price=x['price'], description=x['description'], category=x['category'], quantity=x['quantity'])



        return GetBoxResponse(box=box_details)

    def CreateBox(self, request, context):
        #metadata = dict(context.invocation_metadata())
        #print(metadata)
        box = Box(name=request.name, id=1, price=request.price, description=request.description, category=request.category, quantity=request.quantity)
        #CreateBoxRequest(box=box)
        #if request.name not in books_by_category:
        #   context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        #print(books_by_category)
        #books_for_category = books_by_category[request]
        # num_results = min(request.max_results, len(books_for_category))
        # books_to_recommend = random.sample(
        #     books_for_category
        # )
        #x = mycol.insert_one(books_by_category)
        #print(request)

        return CreateBoxResponse(box=box)

        #return books_by_category

    # def GetBox(self, request, context):
    #     #if request.name not in books_by_category:
    #     #   context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
    #     #print(books_by_category)
    #     #books_for_category = books_by_category[request]
    #     # num_results = min(request.max_results, len(books_for_category))
    #     # books_to_recommend = random.sample(
    #     #     books_for_category
    #     # )

    #     return GetBoxResponse(box=books_by_category)
    #     #return books_by_category


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_DatabaseServiceServicer_to_server(
        DatabaseService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    print("server started")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()