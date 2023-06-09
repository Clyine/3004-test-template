from concurrent import futures
import logging

import grpc
import template_pb2_grpc
import template_pb2

#Create a class that inherits the Servicer object from the generated stub
class TemplateServicer(template_pb2_grpc.TemplateServicer):
    #Implement all endpoints from protofile
    #Should be auto generated by default to return the default values
    def apiEndpoint1(self, request, context):
        #Do something with the request
        accessParam1 = request.params1
        accessParam2 = request.params2
        return template_pb2.resultObj(value1=accessParam1, value2=accessParam2)

#Starts a thread to listen on indicated port
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    #To replace accordingly if Service name changed in protofile
    template_pb2_grpc.add_TemplateServicer_to_server(
        TemplateServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

#runs the thread
if __name__ == '__main__':
    logging.basicConfig()
    serve()