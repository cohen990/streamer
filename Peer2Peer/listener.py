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
        olddata = ""
        data = recv_end(clientsocket).decode()
        print "All data received!"
        r='Receieved!'
        clientsocket.send(r.encode())
        print "responded with ", r.encode().decode()