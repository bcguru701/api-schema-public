# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: grpc/lb/v1/load_balancer.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.protobuf.duration_pb2
import google.protobuf.timestamp_pb2
import grpc.lb.v1.load_balancer_pb2


class LoadBalancerBase(abc.ABC):

    @abc.abstractmethod
    async def BalanceLoad(self, stream: 'grpclib.server.Stream[grpc.lb.v1.load_balancer_pb2.LoadBalanceRequest, grpc.lb.v1.load_balancer_pb2.LoadBalanceResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/grpc.lb.v1.LoadBalancer/BalanceLoad': grpclib.const.Handler(
                self.BalanceLoad,
                grpclib.const.Cardinality.STREAM_STREAM,
                grpc.lb.v1.load_balancer_pb2.LoadBalanceRequest,
                grpc.lb.v1.load_balancer_pb2.LoadBalanceResponse,
            ),
        }


class LoadBalancerStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.BalanceLoad = grpclib.client.StreamStreamMethod(
            channel,
            '/grpc.lb.v1.LoadBalancer/BalanceLoad',
            grpc.lb.v1.load_balancer_pb2.LoadBalanceRequest,
            grpc.lb.v1.load_balancer_pb2.LoadBalanceResponse,
        )