
import socket
from networkData import *
from moraba import *
from data import *
from board import printOut, cowSay, colors


SERVER_SOCKET=socket.socket();
NETWORK_DATA= Network_data()
NUM_PLAYERS=0
PLAYER_SOCK_ID=[]

def create_server_socket():
    global SERVER_SOCKET
    HOST=socket.gethostbyname(socket.getfqdn())
    print("Host: {0}\n".format(HOST))
    PORT=socket.htons(SERVER_PORT)
    ADDR=(HOST,PORT)
    SERVER_SOCKET.bind(ADDR)

def runGameServer(game):
    game.nextTurn()
    checkStateChange(game.CurrentPlayer)
    #send_clients_game(game)
    printOut(game);


def startGame():
    player1 = Player("player1",'X',12,ThePlayerState.PLACING,[],colors.GREEN,0)
    player2 = Player("player2",'O',12,ThePlayerState.PLACING,[],colors.RED,1)
    board= Board()
    startboard=board.startBoard()
    allBoardMills= board.allBoardMills()
    game= Game(player1,player2,startboard,1,allBoardMills)
    runGameServer(game)



def main():
    global NETWORK_DATA,SERVER_SOCKET,NUM_PLAYERS,PLAYER_SOCK_ID

    create_server_socket()
    SERVER_SOCKET.listen(2)
    print("Server Started\n")

    while (NUM_PLAYERS < 2) :
        print("Waiting for clients...\n")
        client_sock,client_addr= SERVER_SOCKET.accept() 
        print("Got a connection from\n ",client_addr)
        PLAYER_SOCK_ID.append(client_sock)
        player_id= NUM_PLAYERS
        client_sock.send(str(NUM_PLAYERS).encode())
        NUM_PLAYERS+=1

    print("Game can now start!\n")
    
    #tell the players that the game can start

    NETWORK_DATA.SERVER_INSTRUCTION= NETWORK_DATA.getServerInstructionValue(InstructionFromServer.GAME_START)

    PLAYER_SOCK_ID[0].send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())
    PLAYER_SOCK_ID[1].send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())

    startGame()
    PLAYER_SOCK_ID[0].close()
    PLAYER_SOCK_ID[1].close()
    SERVER_SOCKET.close()

main()
