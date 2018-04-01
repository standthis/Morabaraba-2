
import socket
import networkData




SERVER_SOCKET=socket.socket();
NETWORK_DATA= networkData.Network_data()
NUM_PLAYERS=0
PLAYER_SOCK_ID=[]

def create_server_socket():
    global SERVER_SOCKET
    HOST= "127.0.0.1"
    print("Host: {0}\n".format(HOST))
    PORT=socket.htons(networkData.SERVER_PORT)
    ADDR=(HOST,PORT)
    SERVER_SOCKET.bind(ADDR)

def main():
    global SERVER_SOCKET,NUM_PLAYERS
    create_server_socket()
    SERVER_SOCKET.listen(2)
    print("Server Started\n")

    while (NUM_PLAYERS < 2) :
        print("Waiting for clients...\n")
        client_sock,client_addr= SERVER_SOCKET.accept() 
        print("Got a connection from ",client_addr)
        PLAYER_SOCK_ID.append(client_sock);   
        #client_sock.recv()
        player_id= NUM_PLAYERS
        client_sock.send(str(NUM_PLAYERS).encode())
        NUM_PLAYERS+=1

    client_sock.close()

main()
