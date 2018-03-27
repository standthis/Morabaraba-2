from enum import Enum 

class ThePlayerState(Enum):
    MOVING = 0
    PLACING = 1 
    FLYING = 2


class Player:
    def __init__(self, name, symbol, numberOfCows, playerState, positions):
        self.Name = name 
        self.Symbol =  symbol 
        self.NumberOfCows = numberOfCows
        self.PlayerState = playerState 
        self.Positions = positions 

class Cow: 
    def __init__(self, pos, symbol, possibleMoves):
        self.Pos = pos 
        self.Symbol = symbol 
        self.PossibleMoves = possibleMoves 

class Board:
    A1 = Cow(('A', 1), ' ', [])
    A4 = Cow(('A', 4), ' ', [])
    A7 = Cow(('A', 7), ' ', [])

    B2 = Cow(('B', 2), ' ', [])
    B4 = Cow(('B', 4), ' ', [])
    B6 = Cow(('B', 6), ' ', [])

    C3 = Cow(('C', 3), ' ', [])
    C4 = Cow(('C', 4), ' ', [])
    C5 = Cow(('C', 5), ' ', [])

    D1 = Cow(('D', 1), ' ', [])
    D2 = Cow(('D', 2), ' ', [])
    D3 = Cow(('D', 3), ' ', [])

    D5 = Cow(('D', 5), ' ', [])
    D6 = Cow(('D', 6), ' ', [])
    D7 = Cow(('D', 7), ' ', [])

    E3 = Cow(('E', 3), ' ', [])
    E4 = Cow(('E', 4), ' ', [])
    E5 = Cow(('E', 5), ' ', [])

    F2 = Cow(('F', 2), ' ', [])
    F4 = Cow(('F', 4), ' ', [])
    F6 = Cow(('F', 6), ' ', [])

    G1 = Cow(('G', 1), ' ', [])
    G4 = Cow(('G', 4), ' ', [])
    G7 = Cow(('G', 7), ' ', [])

    def startBoard():

        A1.PossibleMoves = [A4, B2, D1]
        A4.PossibleMoves = [A1, A7, B4]
        A7.PossibleMoves = [A4, B6, D7]

        B2.PossibleMoves = [A1, B4, C3, D2]
        B4.PossibleMoves = [A4, B2, B6, C4]
        B6.PossibleMoves = [A7, B4, D6, C5]

        C3.PossibleMoves = [B2, C4, D3]
        C4.PossibleMoves = [B4, C3, C5]
        C5.PossibleMoves = [B6, C4, D5]

        D1.PossibleMoves = [A1, D2, G1]
        D2.PossibleMoves = [B2, D1, D3, F2] 
        D3.PossibleMoves = [C3, D2, E3]

        D5.PossibleMoves = [C5, D6, E5]
        D6.PossibleMoves = [B6, D5, D7, F6]
        D7.PossibleMoves = [A7, D6, G7]

        E3.PossibleMoves = [D3, F2, E4]
        E4.PossibleMoves = [E3, F4, E5]
        E5.PossibleMoves = [D5, E4, F6]

        F2.PossibleMoves = [D2, E3, F4, G1]
        F4.PossibleMoves = [E4, F2, F6, G4]
        F6.PossibleMoves = [D6, E5, F4, G7]

        G1.PossibleMoves = [D1, F2, G4]
        G4.PossibleMoves = [F4, G1, G7]
        G7.PossibleMoves = [D7, F6, G4]

        return [A1, A4, A7, B2, B4, B6, C3, C4, C5, D1, D2, D3, D5, D6, D7, E3, E4, E5, F2, F4, F6, G1, G4, G7]

    def allBoardMills():

        AA17 = [A1, A4, A7]
        BB26 = [B2, B4, B6]
        CC35 = [C3, C4, C5]
        DD13 = [D1, D2, D3]
        DD57 = [D5, D6, D7]
        EE35 = [E3, E4, E5]
        FF26 = [F2, F4, F6]
        GG17 = [G1, G4, G7]

        AG11 = [A1, D1, G1]
        BF22 = [B2, D2, F2]
        CE33 = [C3, D3, E3]
        AC44 = [A4, B4, C4]
        EG44 = [E4, F4, G4]
        CE55 = [C5, D5, E5]
        BF66 = [B6, D6, F6]
        AG77 = [A7, D7, G7]

        AC13 = [A1, B2, C3]
        CA57 = [C5, B6, A7]
        GE13 = [G1, F2, E3]
        EG57 = [E5, F6, G7]

        allBoardMills = [ AA17, BB26, CC35, DD13, DD57, EE35, FF26, GG17, AG11, BF22, CE33, AC44, EG44, CE55, BF66, AG77, AC13, CA57, GE13, EG57 ]

        return allBoardMills


#    def getPlayerMove(avaiableBoard, player): 

class Game: 
    def __init__(self, player1, player2, board, turn):
        self.Player1 = player1
        self.Player2 = player2
        self.Board = board
        self.Turn = turn 


    def availableBoard(board):
        result = []
        for i in range(len(board)):
            if board[i].Symbol == ' ':
                result.append(board[i])
        return result

