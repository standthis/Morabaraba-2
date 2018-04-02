
import socket
from networkData import *
from moraba import *
from data import *
from board import printOut, cowSay, colors


SERVER_SOCKET =socket.socket();
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

def write_to_player(whichPlayer):
    fromLet, fromNum = NETWORK_DATA.fromPos
    toLet,toPos = NETWORK_DATA.toPos
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.CLIENT_INSTRUCTION).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.latest_player_id).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.current_player_id).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(fromLet).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(fromNum).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(toLet).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(toPos).encode())

def read_from_player(whichPlayer):
    NETWORK_DATA.CLIENT_INSTRUCTION= int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.SERVER_INSTRUCTION= int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.latest_player_id= int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())

    NETWORK_DATA.current_player_id= int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.fromPos= (PLAYER_SOCK_ID[whichPlayer].recv(1).decode()), int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.toPos= (PLAYER_SOCK_ID[whichPlayer].recv(1).decode()) , int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())


def process_instruction_fromClient(game):
   # global NETWORK_DATA
    if(NETWORK_DATA.CLIENT_INSTRUCTION == NETWORK_DATA.getClientInstructionValue(InstructionFromClient.PLAYER_MOVE)):
        fromPos= NETWORK_DATA.fromPos;
        toPos= NETWORK_DATA.toPos
        if(game.CurrentPlayer.PlayerState==ThePlayerState.PLACING):
            print("Pos to move is ",toPos)
            game.CurrentPlayer.addCow(Game.findCow(toPos, game.availableBoard()))
        
        NETWORK_DATA.SERVER_INSTRUCTION= NETWORK_DATA.getServerInstructionValue(InstructionFromServer.DO_NOTHING)
            
        write_to_player(game.CurrentPlayer.ID);
            
        print("{0} just played\n".format(game.CurrentPlayer.Name));
            
        NETWORK_DATA.SERVER_INSTRUCTION= NETWORK_DATA.getServerInstructionValue(InstructionFromServer.MOVE_PIECE)
        write_to_player(game.OtherPlayer.ID);

    #else:
        #toDO
        
def send_clients_game(game):
    read_from_player(game.CurrentPlayer.ID)
    process_instruction_fromClient(game)
    
def runGameServer(game):
    game.nextTurn()
    checkStateChange(game.CurrentPlayer)
    send_clients_game(game)
    printOut(game);


def startGame():
    player1 = Player("player1",'X',12,ThePlayerState.PLACING,[],colors.GREEN,0)
    player2 = Player("player2",'O',12,ThePlayerState.PLACING,[],colors.RED,1)
    board= Board()
    startboard=board.startBoard()
    allBoardMills= board.allBoardMills()
    game= Game(player1,player2,startboard,1,allBoardMills)
    while not game.endGame():
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
