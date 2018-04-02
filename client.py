import socket
from networkData import *
from moraba import *
from data import *
from board import colors ,printOut

PLAYER_ID = 0
SOCKET = socket.socket()
NETWORK_DATA = Network_data()

def connect_to_server(ip_address):
    global SOCKET
    PORT= socket.htons(SERVER_PORT)
    ADDR=(ip_address,PORT)
    SOCKET.connect(ADDR);

def get_player_id():
   return int(SOCKET.recv(1).decode())  #player id is only 1 byte cause its a string version of a single digit number

def runServerGame(game:Game):
    game.nextTurn()
    checkStateChange(game.CurrentPlayer)
    printOut(game)
    if(game.CurrentPlayer.ID==PLAYER_ID):
        print("Your turn")
    else:
        print("Currently {0}'s turn\n".format(game.CurrentPlayer.Name))


def startGame():
    player1=Player("player1",'X',12,ThePlayerState.PLACING,[],colors.GREEN,0)
    player2=Player("player2",'O',12,ThePlayerState.PLACING,[],colors.RED,1)
    board=Board()
    startboard=board.startBoard()
    allBoardMills= board.allBoardMills()
    game= Game(player1,player2,startboard,1,allBoardMills)
    runServerGame(game)

def main():
    global PLAYER_ID,SOCKET,NETWORK_DATA
    #ip_address=input("Please enter the ip address for the server:\n").strip()
    ip_address="192.168.1.19"
    connect_to_server(ip_address)
    print("Connected!\n")
    print("You are player {0}\n".format(PLAYER_ID+1))
    if(PLAYER_ID==0):
        print("Waiting for second player...\n");

    PLAYER_ID = get_player_id()
    NETWORK_DATA.SERVER_INSTRUCTION = int(SOCKET.recv(1).decode())
    if(NETWORK_DATA.SERVER_INSTRUCTION == NETWORK_DATA.getServerInstructionValue(InstructionFromServer.GAME_START)):
        startGame()
    else:
        print("Game failed to start\n")
        return 1

   
    SOCKET.close()


main()



