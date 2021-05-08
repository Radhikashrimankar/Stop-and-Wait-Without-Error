import socket
from random import randint
import pickle
import sys
from time import sleep
trans = 0
f = open('test.txt','r')
seq = 0
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#port = int(sys.argv[1])
port = 6100
sock.bind(('',port))
sock.listen(2)
conn,addr = sock.accept()
print ('connection received from :',addr)
msg = f.read(512)

while msg:
    data = [seq,msg]
    dat = pickle.dumps(data)
    conn.send(dat)
   #print msg
    print ('sent packet::',seq)

    rep = conn.recv(512)


    if seq == 1:
        print ('received ack for pkt no ::',seq)
        seq = 0
    elif seq == 0:
        print ('received ack for pkt no ::',seq)
        seq = 1
    msg = f.read(512)

print ('All Packets sent successfully !!')

f.close()
conn.close()
sock.close()
