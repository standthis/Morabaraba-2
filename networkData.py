SERVER_PORT = 5151

class InstructionFromClient:
    PLAYER_MOVE = 0
    KILL_COW = 1
    NO_KILL_COW = 2

class InstructionFromServer: 
    DO_NOTHING = 0
    MOVE_PIECE = 1
    REMOVE_PIECE = 2
    GAME_START = 3

class Network_data:

    def __init__(self):
        self.CLIENT_INSTRUCTION = 0
        self.SERVER_INSTRUCTION = 0
        self.latest_player_id = 0
        self.current_player_id = 0
        self.fromPos = ('', 0)
        self.toPos = ('', 0)
