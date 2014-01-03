#! /usr/bin/env python3
import sys

def main(argv):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('192.168.30.102', 8202))
    while True:
        msg = sock.recv(2048)
        if msg:
            print(msg)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
