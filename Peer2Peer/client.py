import socket

def recv_end(sender):
    total_data=[]
    data=''
    End = "END"
    while True:
            data=sender.recv(8192)
            if End in data:
                total_data.append(data[:data.find(End)])
                break
            total_data.append(data)
            if len(total_data)>1:
                #check if end_of_data was split
                last_pair=total_data[-2]+total_data[-1]
                if End in last_pair:
                    total_data[-2]=last_pair[:last_pair.find(End)]
                    total_data.pop()
                    break
    return ''.join(total_data)

ipAddress = "192.168.1.205"
port = 6699
socketLocation = (ipAddress, port)

client = socket.socket();
client.connect(socketLocation)

print "Connected to port:", port

message = "Hello"
client.send(message)
client.send("END")

while(1):
    response = recv_end(client)
    if(response):
        print response
        break