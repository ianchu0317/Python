import socket

from server import MSG_BUFF

CLIENT_ADDRESS = ("127.0.0.1", 4444)
SERVER_ADDRESS = ("127.0.0.1", 4444)
MSG_BUFF = 1024

def printMessage(addr, msg):
    print("{}: {}".format(addr, msg))

def main():
    # Create socket and connect to server
    c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_socket.connect(SERVER_ADDRESS)
    
    CONNECTED = True

    while CONNECTED:
        message = str(c_socket.recv(MSG_BUFF), "utf-8")
        printMessage(SERVER_ADDRESS[0], message)
        toSend = input("{}: ".format(CLIENT_ADDRESS[0]))
        c_socket.send(bytes(toSend, "utf-8"))
        if toSend == "quit":
            CONNECTED = False
  
    c_socket.close()
    print("Exit from server !")

if __name__ == '__main__':
    main()