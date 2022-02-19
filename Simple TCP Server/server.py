from re import S
import socket
import threading

SERVER_ADDRESS = ("127.0.0.1", 4444)
MSG_BUFF = 1024

def getData():
    return input(f"{SERVER_ADDRESS[0]}: ")

def printMessage(addr, msg):
    print("{}: {}".format(addr, msg))

def handleConnection(clientSocket, clientAddress):
    CONNECTED = True
    CLIENT_IP = clientAddress[0]
    print("{} has connected !".format(CLIENT_IP))
    clientSocket.send(bytes(f"You're connected to {SERVER_ADDRESS[0]} !", "utf-8"))

#    message = str(clientSocket.recv(MSG_BUFF), "utf-8")
#    print(f"{CLIENT_IP} : {message}")
    while CONNECTED:
        message = str(clientSocket.recv(MSG_BUFF), "utf-8")
        printMessage(CLIENT_IP, message)
        
        if message == 'quit':
            CONNECTED = False

        data = getData()
        clientSocket.send(bytes(data, "utf-8"))
    
    clientSocket.close()
    return


def main():
    # Create and listen in local computer
    s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_socket.bind(SERVER_ADDRESS)
    s_socket.listen(1)
    print("Server on {}:{}...".format(SERVER_ADDRESS[0], SERVER_ADDRESS[1]))

    connections = 0
    allConnectionsThread = []

    while connections < 1:
        clientSocket, clientAddress = s_socket.accept()
        connections += 1
        currentConn = threading.Thread(target=handleConnection, args=(clientSocket, clientAddress))
        currentConn.start()
        allConnectionsThread.append(currentConn)

    # Wait for running threads
    print("Active connections: ", connections)    
    for currentConn in allConnectionsThread:
        currentConn.join()

    s_socket.close() # Close server
    print("Server finished :)")


if __name__ == '__main__':
    main()