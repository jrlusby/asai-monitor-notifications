#! /usr/bin/env python3
import sys


def main(argv):
    #real basic code to grab the lines from the yield thing
    for line in listen("192.168.30.102", 8202):
        print(line)

#the yield thing that yields massages (The second of 3 MASSAGE yielders @
#MINDBODY)
def listen(ip_addr, port):
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip_addr, port))
    buff = ""
    start = "<?xml version='1.0' encoding='ISO-8859-1'?>"
    stop = "</sps:DataMsg>"
    while True:
        recv = str(sock.recv(2048))
        if recv:
            buff = buff + recv
            if start in buff and stop in buff:
                msg = buff[buff.find(start):buff.find(stop)+len(stop)]
                buff = buff[buff.find(stop)+len(stop):]
                yield msg

def parseEventData(ip_addr, port):
    start = "<sps:EventData>"
    stop = "</sps:EventData>"
    for line in listen(ip_addr, port):
        if start in line and stop in line:
            yield (line, line[line.find(start)+len(start):line.find(stop)])
        else:
            yield (line, "no event data")

if __name__ == '__main__':
    sys.exit(main(sys.argv))
