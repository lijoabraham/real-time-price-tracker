# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import realtime_data_pb2 as realtime__data__pb2


class RealTimeDataServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetData = channel.unary_stream(
                '/realtime_data.RealTimeDataService/GetData',
                request_serializer=realtime__data__pb2.RealTimeDataRequest.SerializeToString,
                response_deserializer=realtime__data__pb2.RealTimeDataResponse.FromString,
                )


class RealTimeDataServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RealTimeDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetData': grpc.unary_stream_rpc_method_handler(
                    servicer.GetData,
                    request_deserializer=realtime__data__pb2.RealTimeDataRequest.FromString,
                    response_serializer=realtime__data__pb2.RealTimeDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'realtime_data.RealTimeDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RealTimeDataService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/realtime_data.RealTimeDataService/GetData',
            realtime__data__pb2.RealTimeDataRequest.SerializeToString,
            realtime__data__pb2.RealTimeDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
