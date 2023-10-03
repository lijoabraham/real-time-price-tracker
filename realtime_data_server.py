import grpc
import time
import json
from concurrent import futures
from kafka_con import KafkaConsumer
from realtime_data_pb2 import RealTimeDataResponse
from realtime_data_pb2_grpc import RealTimeDataServiceStub, RealTimeDataServiceServicer, add_RealTimeDataServiceServicer_to_server

class RealTimeDataServicer(RealTimeDataServiceServicer):

    def GetData(self, request, context):
        try:
            # message = json.dumps({'message' : f'test{time.time()}'})
            # response = RealTimeDataResponse(data=message)
            # yield response
            # Initialize Kafka consumer to subscribe to CDC events
            # kafka_consumer = KafkaConsumer(
            #     'dbserver1.inventory.customers',  # Replace with your CDC Kafka topic
            #     bootstrap_servers='localhost:9092',  # Specify your Kafka broker(s)
            #     group_id='realtime_data_consumer',
            #     # auto_offset_reset='earliest',
            #     enable_auto_commit=True,
            #     auto_commit_interval_ms=1000,
            # )

            # for kafka_message in kafka_consumer:
            #     cdc_event = kafka_message.value.decode('utf-8')  # Deserialize CDC event
            #     message = cdc_event if cdc_event else []
            #     # Process and convert CDC event to gRPC response
            #     response = RealTimeDataResponse(data=message)
            #     yield response
            # kafka_consumer.close()
            cdc_event = []
            with open('ids.txt') as file:
                lines = [line.rstrip() for line in file]
            for line in lines:
                response = RealTimeDataResponse(data=json.dumps(line))
                yield response
        except grpc.RpcError as e:
            # Handle gRPC exceptions
            if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
                print("Invalid argument error:", e.details())
            elif e.code() == grpc.StatusCode.NOT_FOUND:
                print("Not found error:", e.details())
            else:
                print("Unknown error:", e.code(), e.details())

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_RealTimeDataServiceServicer_to_server(RealTimeDataServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
