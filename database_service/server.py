from concurrent import futures
import random

import grpc

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
)

import db_pb2_grpc


# books_by_category = [Box(name='box1', id=2, price=20, description='disc', category='cat', quantity=9),
# Box(name='box2', id=3, price=20, description='disce', category='cate', quantity=10)
# ]

books_by_category = Box(name='box1', id=2, price=20, description='disc', category='cat', quantity=9)
    # BookCategory.MYSTERY: [
    #     BookRecommendation(id=1, title="The Maltese Falcon"),
    #     BookRecommendation(id=2, title="Murder on the Orient Express"),
    #     BookRecommendation(id=3, title="The Hound of the Baskervilles"),
    # ],
  
  



class DatabaseService(
    db_pb2_grpc.DatabaseServiceServicer
):
    def GetBox(self, request, context):
        #if request.name not in books_by_category:
        #   context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")
        #print(books_by_category)
        #books_for_category = books_by_category[request]
        # num_results = min(request.max_results, len(books_for_category))
        # books_to_recommend = random.sample(
        #     books_for_category
        # )

        return GetBoxResponse(box=books_by_category)
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