import socket
from networkData import *
from moraba import *
from data import *
from board import printOut, colors

SERVER_SOCKET = socket.socket();
NETWORK_DATA = Network_data()
NUM_PLAYERS = 0
PLAYER_SOCK_ID = []
PORT = 0

def create_server_socket():
    global SERVER_SOCKET, PORT
    HOST = socket.gethostbyname(socket.getfqdn())
    print("                             IP address: {0}\n".format(HOST))
    PORT = socket.htons(SERVER_PORT)
    ADDR = (HOST,PORT)
    SERVER_SOCKET.bind(ADDR)

def write_to_player(whichPlayer):
    fromLet, fromNum = NETWORK_DATA.fromPos
    toLet, toPos = NETWORK_DATA.toPos
    
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.CLIENT_INSTRUCTION).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.latest_player_id).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(NETWORK_DATA.current_player_id).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(fromLet).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(fromNum).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(toLet).encode())
    PLAYER_SOCK_ID[whichPlayer].send(str(toPos).encode())

def read_from_player(whichPlayer):
    NETWORK_DATA.CLIENT_INSTRUCTION = int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.SERVER_INSTRUCTION = int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.latest_player_id = int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())

    NETWORK_DATA.current_player_id = int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.fromPos = (PLAYER_SOCK_ID[whichPlayer].recv(1).decode()), int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())
    NETWORK_DATA.toPos = (PLAYER_SOCK_ID[whichPlayer].recv(1).decode()), int(PLAYER_SOCK_ID[whichPlayer].recv(1).decode())

def process_instruction_fromClient(game):
    fromPos = NETWORK_DATA.fromPos
    toPos = NETWORK_DATA.toPos
    if(NETWORK_DATA.CLIENT_INSTRUCTION == InstructionFromClient.PLAYER_MOVE):
        
        if(game.CurrentPlayer.PlayerState == ThePlayerState.PLACING):
            print("{0} is moving to {1}".format(game.CurrentPlayer.Name, toPos))
            game.CurrentPlayer.addCow(Game.findCow(toPos, game.availableBoard()))
        
        else: #player is has to be MOVING or FLYING
            game.CurrentPlayer.removeCow(Game.findCow(fromPos, game.CurrentPlayer.Cows))
            game.CurrentPlayer.addCow(Game.findCow(toPos, game.availableBoard()))
        
        NETWORK_DATA.SERVER_INSTRUCTION = InstructionFromServer.DO_NOTHING
            
        write_to_player(game.CurrentPlayer.ID)
            
        print("{0} just played\n".format(game.CurrentPlayer.Name))
            
        NETWORK_DATA.SERVER_INSTRUCTION = InstructionFromServer.MOVE_PIECE
        write_to_player(game.OtherPlayer.ID)

    elif(NETWORK_DATA.CLIENT_INSTRUCTION == InstructionFromClient.KILL_COW):
        game.OtherPlayer.removeCow(Game.findCow(toPos, game.OtherPlayer.Cows))
        NETWORK_DATA.SERVER_INSTRUCTION = InstructionFromServer.DO_NOTHING

        write_to_player(game.CurrentPlayer.ID)

        print("{0} has shot cow at {1}".format(game.CurrentPlayer.Name, toPos))
        
        NETWORK_DATA.SERVER_INSTRUCTION = InstructionFromServer.REMOVE_PIECE
        write_to_player(game.OtherPlayer.ID)
        
    elif(NETWORK_DATA.CLIENT_INSTRUCTION == InstructionFromClient.NO_KILL_COW):
        NETWORK_DATA.SERVER_INSTRUCTION = InstructionFromServer.DO_NOTHING
        write_to_player(game.CurrentPlayer.ID)
        write_to_player(game.OtherPlayer.ID)
        
def get_clients_game(game):
    read_from_player(game.CurrentPlayer.ID)
    process_instruction_fromClient(game)
    toPos = NETWORK_DATA.toPos
    
    if(Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills)):
        print("{0} has formed a mill ".format(game.CurrentPlayer.Name))
        game.Board = game.getCurrentBoard()
        printOut(game)

    read_from_player(game.CurrentPlayer.ID) #check for mill formed
    process_instruction_fromClient(game)
    game.Board = game.getCurrentBoard()
   
def runGameServer(game):
    game.nextTurn()
    checkStateChange(game.CurrentPlayer)
    get_clients_game(game)
    printOut(game)

def startGame():
    player1 = Player("Player 1", 'X', 12, ThePlayerState.PLACING, [], colors.GREEN, 0)
    player2 = Player("Player 2", 'O', 12, ThePlayerState.PLACING, [], colors.RED, 1)
    board = Board()
    startboard = board.startBoard()
    allBoardMills = board.allBoardMills()
    game = Game(player1, player2, startboard, 1, allBoardMills)
    
    while not game.endGame():
        runGameServer(game)

def main():
    morabarabaWord = '''
                ___  ___                _                     _           
                |  \/  |               | |                   | |          
                | .  . | ___  _ __ __ _| |__   __ _ _ __ __ _| |__   __ _ 
                | |\/| |/ _ \| '__/ _` | '_ \ / _` | '__/ _` | '_ \ / _` |
                | |  | | (_) | | | (_| | |_) | (_| | | | (_| | |_) | (_| |
                \_|  |_/\___/|_|  \__,_|_.__/ \__,_|_|  \__,_|_.__/ \__,_|
    '''
    print(morabarabaWord)
    
    global NETWORK_DATA, SERVER_SOCKET, NUM_PLAYERS, PLAYER_SOCK_ID

    create_server_socket()
    SERVER_SOCKET.listen(2)
    print("                             Server Started on port {0} \n".format(PORT))

    while (NUM_PLAYERS < 2) :
        print("                             Waiting for clients...\n")
        client_sock, client_addr = SERVER_SOCKET.accept() 
        print("                             Got a connection from\n ", client_addr)
        PLAYER_SOCK_ID.append(client_sock)
        client_sock.send(str(NUM_PLAYERS).encode())
        NUM_PLAYERS += 1

    print("                             Game can now start!\n")
    
    #tell the players that the game can start
    NETWORK_DATA.SERVER_INSTRUCTION = InstructionFromServer.GAME_START

    PLAYER_SOCK_ID[0].send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())
    PLAYER_SOCK_ID[1].send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())

    startGame()
    
    PLAYER_SOCK_ID[0].close()
    PLAYER_SOCK_ID[1].close()
    SERVER_SOCKET.close()

main()
