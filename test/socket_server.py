# -*- coding: utf-8 -*-
import socket
import threading
import time
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
server.bind(("localhost", 9998))
server.listen(5)
print("等待客户端连接...")
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)
while True:
    sock, addr = server.accept()
    print("新连接：", addr)
    # data = sock.recv(1024)
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    # if not data:
    #     break
    # print("收到消息：", data)
    # sock.send(data.upper())
    # if data == str("close"):
    #     server.close()