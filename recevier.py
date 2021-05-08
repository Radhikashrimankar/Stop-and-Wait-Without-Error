import socket
import pickle
import sys

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
seq = 1
port = 6100
sock.connect(('       ',port))


f = open('an.txt','w')
msg = sock.recv(1024)
while msg:
    data = pickle.loads(msg)
    print ('packet ',data[0],' received...')
    f.write(data[1])
    sock.send(b'data[1]')
    msg = sock.recv(1024)

f.close()
