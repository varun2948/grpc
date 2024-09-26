import grpc
import test_pb2
import test_pb2_grpc
from concurrent import futures


class SquareServiceServicer(test_pb2_grpc.SquareServiceServicer):
    def square(self, request, context):
        result = request.input * request.input
        return test_pb2.Result(result=result)


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    test_pb2_grpc.add_SquareServiceServicer_to_server(SquareServiceServicer(), server)
    print("Starting server. Listening on port 50051.")
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


main()
