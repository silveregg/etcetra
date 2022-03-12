# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import v3lock_pb2 as v3lock__pb2


class LockStub(object):
    """The lock service exposes client-side locking facilities as a gRPC interface.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Lock = channel.unary_unary(
                '/v3lockpb.Lock/Lock',
                request_serializer=v3lock__pb2.LockRequest.SerializeToString,
                response_deserializer=v3lock__pb2.LockResponse.FromString,
                )
        self.Unlock = channel.unary_unary(
                '/v3lockpb.Lock/Unlock',
                request_serializer=v3lock__pb2.UnlockRequest.SerializeToString,
                response_deserializer=v3lock__pb2.UnlockResponse.FromString,
                )


class LockServicer(object):
    """The lock service exposes client-side locking facilities as a gRPC interface.
    """

    def Lock(self, request, context):
        """Lock acquires a distributed shared lock on a given named lock.
        On success, it will return a unique key that exists so long as the
        lock is held by the caller. This key can be used in conjunction with
        transactions to safely ensure updates to etcd only occur while holding
        lock ownership. The lock is held until Unlock is called on the key or the
        lease associate with the owner expires.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unlock(self, request, context):
        """Unlock takes a key returned by Lock and releases the hold on lock. The
        next Lock caller waiting for the lock will then be woken up and given
        ownership of the lock.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LockServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Lock': grpc.unary_unary_rpc_method_handler(
                    servicer.Lock,
                    request_deserializer=v3lock__pb2.LockRequest.FromString,
                    response_serializer=v3lock__pb2.LockResponse.SerializeToString,
            ),
            'Unlock': grpc.unary_unary_rpc_method_handler(
                    servicer.Unlock,
                    request_deserializer=v3lock__pb2.UnlockRequest.FromString,
                    response_serializer=v3lock__pb2.UnlockResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v3lockpb.Lock', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Lock(object):
    """The lock service exposes client-side locking facilities as a gRPC interface.
    """

    @staticmethod
    def Lock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v3lockpb.Lock/Lock',
            v3lock__pb2.LockRequest.SerializeToString,
            v3lock__pb2.LockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v3lockpb.Lock/Unlock',
            v3lock__pb2.UnlockRequest.SerializeToString,
            v3lock__pb2.UnlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
