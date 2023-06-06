import grpc
import template_pb2
import template_pb2_grpc

#Initialise a client stub
channel = grpc.insecure_channel('localhost:50051')
stub = template_pb2_grpc.TemplateStub(channel)

#Call api through the stub, input object provided by client stub
print(stub.apiEndpoint1(template_pb2.inputObj(params1=2,params2=5)))