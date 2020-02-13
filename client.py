from socket import *
from threading import Thread
import sys
import traceback
from threading import Thread
import os
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

global ip_address

class Server(Thread):
    def __init__(self,host,port,name):
        Thread.__init__(self)
        self.port = port
        self.host = host
        self.name = name
        self.bufsize = 5555
        self.addr = (host,port)

        self.socket = socket(AF_INET , SOCK_STREAM)
        self.socket.bind(self.addr)

    def run(self):
        self.socket.listen(5)
        while True:
            print ("Waiting for connection..")
            client, caddr = self.socket.accept()
            print ("Connected To"),caddr

            data = client.recv(1024).decode('utf-8')
            print(data)
            filename = data
            filedata=None
            with open(filename, 'r') as f:
                filedata = f.read()
            print(filedata)
            client.send(filedata.encode('utf-8'))
            # filesize = os.path.getsize(filename)
            # self.socket.send(f"{filename}{SEPARATOR}{filesize}".encode())
            # with open(filename, "rb") as f:
            #     for _ in progress:
            #         # read the bytes from the file
            #         bytes_read = f.read(BUFFER_SIZE)
            #         if not bytes_read:
            #             # file transmitting is done
            #             break
            #         # we use sendall to assure transimission in 
            #         # busy networks
            #         self.socket.sendall(bytes_read)
            #         # update the progress bar
            #         progress.update(len(bytes_read))
            print(filename)
            
            if not data:
                continue
            print (data)         


class Client(Thread):
    def __init__(self,host,port,name):
        Thread.__init__(self)
        self.port = port
        self.host = host
        self.name = name
        self.bufsize = 1024
        self.addr = (host,port)

        self.socket = socket(AF_INET , SOCK_STREAM)

    def run(self):
        invalid = True
        while invalid:
            try:
                invalid = False
                self.socket.connect(self.addr)
            except:
                invalid = True

        while True:
            data = input('> ')
            if not data:
                continue
            self.socket.send(str(data).encode("utf-8"))
            if data == "quit":
                self.socket.close()
                break
            ip_address = self.socket.recv(20485).decode("utf-8")
        ip_a = input('>Give the port number you want to connect ')
        invalid = True
        while invalid:
            try:
                invalid = False
                self.socket.connect(("localhost",int(ip_a)))
                p2p_user = self.socket.recv(20485).decode("utf-8")
                print(">You are connected to " + str(p2p_user))
            except:
                invalid = True    
        while True:
            data = input('>Input the file name you want to download')
            if not data:
                continue
            self.socket.send(str(data).encode("utf-8"))
            
            
            
            
                
                
            
                
            

host = "localhost"
p1 = int(input('Enter Port 1 : '))
p2 = int(input('Enter Port 2 : '))
name = input('Enter Your Name: ').strip()


server = Server(host,p2,name)
client = Client(host,p1,name)

server.start()
client.start()

server.join()