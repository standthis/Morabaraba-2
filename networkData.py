from enum import Enum
from __main__ import *

SERVER_PORT=5151
BUFFER_SIZE= 1024

class InstructionFromClient(Enum):
    PLAYER_MOVE = 0
    KILL_COW=1
    NO_KILL_COW=2


class InstructionFromServer(Enum): 
    DO_NOTHING = 0
    MOVE_PIECE = 1
    REMOVE_PIECE = 2
    GAME_START = 3

    
class Network_data:

    def __init__(self):
        self.CLIENT_INSTRUCTION=0
        self.SERVER_INSTRUCTION=0
        self.latest_player_id=0
        self.current_player_id=0
        self.fromPos=('',0)
        self.toPos=('',0)

    def getServerInstructionValue(self,SERVER_INSTRUCTION):
        if(SERVER_INSTRUCTION==InstructionFromServer.DO_NOTHING):
            return 0
        elif (SERVER_INSTRUCTION==InstructionFromServer.MOVE_PIECE):            
            return 1
        elif (SERVER_INSTRUCTION==InstructionFromServer.REMOVE_PIECE):            
            return 2
        elif (SERVER_INSTRUCTION==InstructionFromServer.GAME_START):            
            return 3
    def getClientInstructionValue(self,CLIENT_INSTRUCTION):
        if(CLIENT_INSTRUCTION==InstructionFromClient.PLAYER_MOVE):           
            return 0
        elif(CLIENT_INSTRUCTION==InstructionFromClient.KILL_COW):           
            return 1
        elif(CLIENT_INSTRUCTION==InstructionFromClient.NO_KILL_COW):   
            return 2 



