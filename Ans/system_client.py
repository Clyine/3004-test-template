import grpc
import system_pb2
import system_pb2_grpc

#Initialise a client stub
channel = grpc.insecure_channel('localhost:50051')
stub = system_pb2_grpc.SystemStub(channel)

#Call api through the stub, input object provided by client stub
print(stub.doList(system_pb2.item(itemName="item1")))
print(stub.doList(system_pb2.item(itemName="item2")))
print(stub.doBid(system_pb2.bid(itemName="item1", bidder="Jq", price=10)))
print(stub.doBid(system_pb2.bid(itemName="item1", bidder="Jq", price=5)))
print(stub.doBid(system_pb2.bid(itemName="item1", bidder="Jq", price=0)))
print(stub.doBid(system_pb2.bid(itemName="item3", bidder="Jq", price=5)))
print(stub.doQuery(system_pb2.item(itemName="")))

while True:
    selection = input("Enter 1 for List, 2 for Bid, 3 for Query: ")
    
    if selection == "1":
        itemName = input("Enter item name: ")
        print(stub.doList(system_pb2.item(itemName=itemName)))
    elif selection == "2":
        itemName = input("Enter item name: ")
        bidder = input("Enter your name: ")
        price = input("Enter desired bid price: ")
        print(stub.doBid(system_pb2.bid(itemName=itemName, bidder=bidder, price=int(price))))
    elif selection == "3":
        print(stub.doQuery(system_pb2.item(itemName="")))
        
    print()
    print("Thank you")
        