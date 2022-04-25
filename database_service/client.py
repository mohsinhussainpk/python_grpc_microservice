import grpc
from db_pb2_grpc import DatabaseServiceStub
from db_pb2 import Box

channel = grpc.insecure_channel("localhost:50051")
client = DatabaseServiceStub(channel)

request = Box()

print(client.GetBox(request))
