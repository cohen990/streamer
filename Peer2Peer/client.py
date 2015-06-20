import socket


ipAddress = socket.gethostbyname(socket.gethostname())
port = 6699
socketLocation = (ipAddress, port)

client = socket.socket();
client.connect(socketLocation)

print "Connected to port:", port

message = ""

for i in xrange(1,1024):
    message += `i` + ": hello\n"
client.send(message)