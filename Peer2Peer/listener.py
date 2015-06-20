import socket


ipAddress = socket.gethostbyname(socket.gethostname())
port = 6699
socketLocation = (ipAddress, port)
listener = socket.socket();
listener.bind(socketLocation)
listener.listen(5)

print "Listening on port:", port

while(1):
    (clientsocket, address) = listener.accept()
    if(clientsocket):
        print ("connection found!")
        data = clientsocket.recv(1024).decode()
        while(data):
            print (data)
            data = clientsocket.recv(1024).decode()
        r='REceieve'
        clientsocket.send(r.encode())