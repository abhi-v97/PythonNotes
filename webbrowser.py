import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
mysock.connect(('data.pr4e.org', 80)) # make the connection to port 80 on server www.py4e.com
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() # GET command according to HTTP protocol
mysock.send(cmd)

while True:
        data = mysock.recv(512) # loop to recceive data in 512 character chunks from sockets
        if (len(data) < 1): # print until there's no more data
            break
        print(data.decode(),end='')
mysock.close()