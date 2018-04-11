import socket
from networkData import *
from moraba import *
from data import *
from board import colors, printOut

PLAYER_ID = 0
SOCKET = socket.socket()
NETWORK_DATA = Network_data()

def connect_to_server(ip_address):
    global SOCKET
    PORT = socket.htons(SERVER_PORT)
    ADDR = (ip_address, PORT)
    SOCKET.connect(ADDR);

def get_player_id():
   return int(SOCKET.recv(1).decode())  #player id is only 1 byte cause its a string version of a single digit number

def write_to_server():
    fromLet, fromNum = NETWORK_DATA.fromPos
    toLet, toNum = NETWORK_DATA.toPos

    SOCKET.send(str(NETWORK_DATA.CLIENT_INSTRUCTION).encode())
    SOCKET.send(str(NETWORK_DATA.SERVER_INSTRUCTION).encode())
    SOCKET.send(str(NETWORK_DATA.latest_player_id).encode())
    SOCKET.send(str(NETWORK_DATA.current_player_id).encode())
    SOCKET.send(str(fromLet).encode())
    SOCKET.send(str(fromNum).encode())
    SOCKET.send(str(toLet).encode())
    SOCKET.send(str(toNum).encode())
  
def read_from_server():
    fromLet, fromNum = NETWORK_DATA.fromPos
    toLet, toPos = NETWORK_DATA.toPos
    
    NETWORK_DATA.CLIENT_INSTRUCTION = int(SOCKET.recv(1).decode())
    NETWORK_DATA.SERVER_INSTRUCTION = int(SOCKET.recv(1).decode())
    NETWORK_DATA.latest_player_id = int(SOCKET.recv(1).decode())
    NETWORK_DATA.current_player_id = int(SOCKET.recv(1).decode())
    NETWORK_DATA.fromPos = (SOCKET.recv(1).decode())[0], int(SOCKET.recv(1).decode())
    NETWORK_DATA.toPos = (SOCKET.recv(1).decode())[0], int(SOCKET.recv(1).decode())

def send_instruction_to_server():
    write_to_server()
    read_from_server()

def process_instruction_from_server(game:Game):
    fromPos = NETWORK_DATA.fromPos
    toPos = NETWORK_DATA.toPos

    if (NETWORK_DATA.SERVER_INSTRUCTION == InstructionFromServer.MOVE_PIECE):
        
        if(game.CurrentPlayer.PlayerState == ThePlayerState.PLACING):
            print("{0} moved to {1} ".format(game.CurrentPlayer.Name, toPos))
            game.CurrentPlayer.addCow(Game.findCow(toPos, game.availableBoard()))
        else:
            print("{0} moved from {1} to {2} ".format(game.CurrentPlayer.Name, fromPos, toPos))
            game.CurrentPlayer.removeCow(Game.findCow(fromPos, game.CurrentPlayer.Cows))
            game.CurrentPlayer.addCow(Game.findCow(toPos, game.availableBoard()))
            
    elif (NETWORK_DATA.SERVER_INSTRUCTION == InstructionFromServer.DO_NOTHING):
        print("")
    elif (NETWORK_DATA.SERVER_INSTRUCTION == InstructionFromServer.REMOVE_PIECE):
        print("{0} just shot your cow at {1}".format(game.CurrentPlayer.Name, toPos))     
        game.OtherPlayer.removeCow(Game.findCow(toPos, game.OtherPlayer.Cows))
    else:      
        print("Invalid instruction!\n", NETWORK_DATA.SERVER_INSTRUCTION);
    
def runServerGame(game:Game):
    game.nextTurn()
    checkStateChange(game.CurrentPlayer)
    printOut(game)
    
    if(game.CurrentPlayer.ID == PLAYER_ID):
        print("Your turn")
        fromPos, toPos = getPlayerMove(game.CurrentPlayer, game.availableBoard(), game.AllBoardMills)
        
        NETWORK_DATA.fromPos = fromPos
        NETWORK_DATA.toPos = toPos
        NETWORK_DATA.CLIENT_INSTRUCTION = InstructionFromClient.PLAYER_MOVE
        
        send_instruction_to_server()
        process_instruction_from_server(game)
        NETWORK_DATA.CLIENT_INSTRUCTION = InstructionFromClient.NO_KILL_COW 
        
        if Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills):
            game.Board = game.getCurrentBoard()
            printOut(game)
            killPos = killCow(game)

            NETWORK_DATA.toPos = killPos #use toPos as the kill Pos
            NETWORK_DATA.CLIENT_INSTRUCTION = InstructionFromClient.KILL_COW
            
        send_instruction_to_server()
        process_instruction_from_server(game)

        checkStateChange(game.OtherPlayer)
       
    else:
        print("Currently {0}'s turn\n".format(game.CurrentPlayer.Name),flush=True)
        #wait to get response from server
        read_from_server() #read to check where other player placed
        process_instruction_from_server(game)
        toPos = NETWORK_DATA.toPos
        
        if(Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills)):
            print("{0} has formed a mill ".format(game.CurrentPlayer.Name))
            game.Board = game.getCurrentBoard()
            printOut(game)
            
        read_from_server() #see if enemy player has formed a mill
        process_instruction_from_server(game)
   
def startGame():
    player1 = Player("player1", 'X', 12, ThePlayerState.PLACING, [], colors.GREEN, 0)
    player2 = Player("player2", 'O', 12, ThePlayerState.PLACING, [], colors.RED, 1)
    board = Board()
    startboard = board.startBoard()
    allBoardMills = board.allBoardMills()
    game = Game(player1, player2, startboard, 1, allBoardMills)
    while not game.endGame(): 
        runServerGame(game)

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
    
    valid = False
    
    while not valid:
        try:
            local = input("                      Are you playing locally? [Y/n] (q to quit): ")[0].upper()
        except: 
            print("                      Please give a valid response!")
            continue
        
        if  local == 'Y' :
            valid = True
            return localMain()
        elif local == 'Q':
            return
        elif local != 'N':
            print("                      Please give a valid response!")
        else:
            valid = True
            
    global PLAYER_ID, SOCKET, NETWORK_DATA
    ip_address = input("                      Please enter the IP address for the server: ").strip()
    connect_to_server(ip_address)
    print("                      Connected!\n")
    PLAYER_ID= get_player_id() 
    print("                      You are player {0}\n".format(PLAYER_ID + 1))
    
    if(PLAYER_ID == 0):
        print("                      Waiting for second player...\n")

    NETWORK_DATA.SERVER_INSTRUCTION = int(SOCKET.recv(1).decode())
    
    if(NETWORK_DATA.SERVER_INSTRUCTION == InstructionFromServer.GAME_START):
        startGame()
    else:
        print("                      Game failed to start\n")
        return 1

    SOCKET.close()

main()
