import socket
import networkData


PLAYER_ID = 0
SOCKET = 0 

def connect_to_server(ip_address):
    global SOCKET
    SOCKET= socket.socket()
    ADDR=(ip_address,networkData.SERVER_PORT)
    SOCKET.connect(ADDR);

def get_player_id():
    return s.recv(networkData.BUFFER_SIZE).decode()

def main():
    global PLAYER_ID
    global SOCKET
    ip_address="127.0.0.1"
    connect_to_server(ip_address)
    print("Connected!\n")
    
    PLAYER_ID = get_player_id()
    
    print("You are player {0}\n".format(PLAYER_ID+1))
    if (PLAYER_ID==0):
        print("Waiting for second player...\n");
    SOCKET.close()




main()
