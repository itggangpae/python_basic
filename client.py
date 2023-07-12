"""
#클라이언트 코드
from socket import *
try:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect(('localhost', 8000))
    sock.send('Hello Server'.encode())
    b = sock.recv(1024)
    print(b.decode())
except Exception as e:
    print("접속 에러:", e)
finally:
    sock.close()
"""

"""
from socket import *
try:
    sock = socket(AF_INET, SOCK_DGRAM)
    msg = input("보낼 메시지:")
    sock.sendto(msg.encode(), ('localhost', 8001))
    s, addr = sock.recvfrom(1024)
    print(s.decode())
    print(addr)
except Exception as e:
    print("접속 에러:", e)
finally:
    sock.close()
"""

"""
from socket import *
try:
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('', 8000))
    msg, addr = sock.recvfrom(1024)
    print(msg.decode())
    print(addr)
except Exception as e:
    print("접속 에러:", e)
finally:
    sock.close()
"""


"""
import socket
from threading import Thread

HOST = 'localhost'
PORT = 9009


def rcvMsg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    t = Thread(target=rcvMsg, args=(sock,))
    t.daemon = True
    t.start()

    while True:
        msg = input()
        if msg == '/quit':
            sock.send(msg.encode())
            break

        sock.send(msg.encode())

runChat()
"""
