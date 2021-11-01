import socket

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM)as HenSuu:
    HenSuu.sendto(b'Hello UDP',('127.0.0.1',50007))