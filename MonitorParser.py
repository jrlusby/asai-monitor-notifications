#! /usr/bin/env python3
import sys

def main(argv):
    for line in listen("192.168.30.102", 8202):
        print(line)

def listen(ip_addr, port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_addr, port))
    while True:
        msg = sock.recv(2048)
        if msg:
            yield msg

if __name__ == '__main__':
    sys.exit(main(sys.argv))
