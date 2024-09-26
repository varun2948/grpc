import grpc
import test_pb2
import test_pb2_grpc


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = test_pb2_grpc.SquareServiceStub(channel)
        response = stub.square(test_pb2.Number(input=10))

    print("Client received: " + str(response.result))

    return response


if __name__ == "__main__":
    run()
