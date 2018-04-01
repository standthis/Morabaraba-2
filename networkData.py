from enum import Enum
from __main__ import *

SERVER_PORT=5151
BUFFER_SIZE= 1024

class InstructionFromClient( Enum):
    PLAYER_MOVE = 0
    KILL_COW=1


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
        self.fromLet=''
        self.fromNum=0
        self.toLet=''
        self.toNum=0
