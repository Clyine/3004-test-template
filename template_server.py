from concurrent import futures
import logging

import grpc
import template_pb2_grpc
import template_pb2


class TemplateServicer(template_pb2_grpc.TemplateServicer):
    def apiEndpoint1(self, request, context):
        accessParam1 = request.params1
        accessParam2 = request.params2
        return template_pb2.resultObj(value1=accessParam1, value2=accessParam2)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    template_pb2_grpc.add_TemplateServicer_to_server(
        TemplateServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()