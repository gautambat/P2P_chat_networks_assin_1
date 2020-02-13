from socket import *
from threading import Thread
import sys
import traceback
from threading import Thread
global ip_address
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

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

            data = client.recv(self.bufsize)
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
                break
            ip_address = self.socket.recv(20485).decode("utf-8")
            print("The Port number for the file asked is " + ip_address)
        
        s = socket(AF_INET , SOCK_STREAM)
        ip_a = int(input('>Port '))
        
        invalid = True
        while invalid:
            try:
                invalid = False
                s.connect(("localhost",ip_a))
            except:
                invalid = True
        while True:
            data = input('> ')
            if not data:
                continue
            self.socket.send(str(data).encode("utf-8"))
            recieve=self.socket.recv(1024)
            print(recieve)
            with open("./filenew.txt", 'w') as f:
                f.write(recieve.decode('utf-8'))
        #     received = self.socket.recv(BUFFER_SIZE).decode()
        #     filename, filesize = received.split(SEPARATOR)
        #     filename = os.path.basename(filename)
        #     filesize = int(filesize)
        #     with open(filename, "wb") as f:
        #         for _ in progress:
        # # read 1024 bytes from the socket (receive)
        #             bytes_read = slef.socket.recv(BUFFER_SIZE)
        #             if not bytes_read:    
        #                 # nothing is received
        #                 # file transmitting is done
        #                 break
        #             # write to the file the bytes we just received
        #             f.write(bytes_read)
        #             # update the progress bar
        #             progress.update(len(bytes_read))

            if data == "quit":
                break
            ip_address = self.socket.recv(20485).decode("utf-8")
            print("The Port number for the file asked is " + ip_address)
            
        
            
            
            
            
                
                
            
                
            

host = "localhost"
p1 = int(input('Enter Port 1 : '))
p2 = int(input('Enter Port 2 : '))
name = input('Enter Your Name: ').strip()


server = Server(host,p2,name)
client = Client(host,p1,name)

server.start()
client.start()

server.join()