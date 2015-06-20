import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ipAddress = get_ip_address('wlan0')
port = 6699
socketLocation = (ipAddress, port)
listener = socket.socket();
listener.bind(socketLocation)
listener.listen(5)

print "Listening on port:", ipAddress, ":", port

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