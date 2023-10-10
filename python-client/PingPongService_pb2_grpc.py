# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import PingPongService_pb2 as PingPongService__pb2


class PingPongServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.say = channel.unary_unary(
                '/com.protocol.grpc.PingPongService/say',
                request_serializer=PingPongService__pb2.SayPingRequest.SerializeToString,
                response_deserializer=PingPongService__pb2.SayPongResponse.FromString,
                )


class PingPongServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def say(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PingPongServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'say': grpc.unary_unary_rpc_method_handler(
                    servicer.say,
                    request_deserializer=PingPongService__pb2.SayPingRequest.FromString,
                    response_serializer=PingPongService__pb2.SayPongResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'com.protocol.grpc.PingPongService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PingPongService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def say(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/com.protocol.grpc.PingPongService/say',
            PingPongService__pb2.SayPingRequest.SerializeToString,
            PingPongService__pb2.SayPongResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)