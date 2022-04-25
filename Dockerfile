FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY database_service/ /service/database_service/
WORKDIR /service/database_service
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=. ../protobufs/db.proto
EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]

