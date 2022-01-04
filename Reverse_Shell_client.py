import  sys 
import socket 

def connect(address):
    try:
        s = socket.socket(sockets)
        s.connect(address)
        print("Connection Established. ")
        print(f"Address {address}")
    except socket.error as error:
        print("Somethings Wrong i can feel it ... ")
        print (error)
        sys.exit()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 52547 
    connect((host,port))