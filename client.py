import socket
import networkData


PLAYER_ID = 0
SOCKET = 0 

def connect_to_server(ip_address):
    global SOCKET
    SOCKET= socket.socket()
    PORT= socket.htons(networkData.SERVER_PORT)
    ADDR=(ip_address,PORT)
    SOCKET.connect(ADDR);

def get_player_id():
   return int(SOCKET.recv(1).decode())  #player id is only 1 byte cause its a string version of a single digit number

def main():
    global PLAYER_ID
    global SOCKET
    #ip_address=input("Please enter the ip address for the server:\n").strip()
    ip_address="192.168.1.19"
    connect_to_server(ip_address)
    print("Connected!\n")
    if (PLAYER_ID==0):
        print("Waiting for second player...\n");

    PLAYER_ID = get_player_id()
    instruction=  SOCKET.recv(networkData.BUFFER_SIZE).decode()
    print("Instruction: {0}".format(instruction))
    print("You are player {0}\n".format(PLAYER_ID+1))

    SOCKET.close()


main()



