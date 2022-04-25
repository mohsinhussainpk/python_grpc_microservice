from concurrent import futures
import random
import pymongo
from dotenv import load_dotenv
import os
import grpc
import db_pb2_grpc

load_dotenv()

MONGO_DB_URL = os.getenv('MONGO_DB_URL')
client = pymongo.MongoClient(MONGO_DB_URL)
mydb = client.pythonGRPC

mycol = mydb["Boxes"]

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

  

class DatabaseService(
    db_pb2_grpc.DatabaseServiceServicer
):
    def GetBox(self, request, context):
        x = mycol.find_one()

        box_details = Box(name=x['name'], id=x['id'], price=x['price'], description=x['description'], category=x['category'], quantity=x['quantity'])



        return GetBoxResponse(box=box_details)





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