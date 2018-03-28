from enum import Enum 
class ThePlayerState(Enum):
    MOVING = 0
    PLACING = 1 
    FLYING = 2


class Player:
    def __init__(self, name, symbol, numberOfCows, playerState, cows):
        self.Name = name 
        self.Symbol = symbol 
        self.NumberOfCows = numberOfCows
        self.PlayerState = playerState 
        self.Cows = cows 

    def addCow(self, cow):
        cow.Symbol = self.Symbol
        self.Cows.append(cow)

    def decrementCows(self):
        self.NumberOfCows -= 1

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

    def startBoard(self):

        self.A1.PossibleMoves = [self.A4, self.B2, self.D1]
        self.A4.PossibleMoves = [self.A1, self.A7, self.B4]
        self.A7.PossibleMoves = [self.A4, self.B6, self.D7]

        self.B2.PossibleMoves = [self.A1, self.B4, self.C3, self.D2]
        self.B4.PossibleMoves = [self.A4, self.B2, self.B6, self.C4]
        self.B6.PossibleMoves = [self.A7, self.B4, self.D6, self.C5]

        self.C3.PossibleMoves = [self.B2, self.C4, self.D3]
        self.C4.PossibleMoves = [self.B4, self.C3, self.C5]
        self.C5.PossibleMoves = [self.B6, self.C4, self.D5]

        self.D1.PossibleMoves = [self.A1, self.D2, self.G1]
        self.D2.PossibleMoves = [self.B2, self.D1, self.D3, self.F2] 
        self.D3.PossibleMoves = [self.C3, self.D2, self.E3]

        self.D5.PossibleMoves = [self.C5, self.D6, self.E5]
        self.D6.PossibleMoves = [self.B6, self.D5, self.D7, self.F6]
        self.D7.PossibleMoves = [self.A7, self.D6, self.G7]

        self.E3.PossibleMoves = [self.D3, self.F2, self.E4]
        self.E4.PossibleMoves = [self.E3, self.F4, self.E5]
        self.E5.PossibleMoves = [self.D5, self.E4, self.F6]

        self.F2.PossibleMoves = [self.D2, self.E3, self.F4, self.G1]
        self.F4.PossibleMoves = [self.E4, self.F2, self.F6, self.G4]
        self.F6.PossibleMoves = [self.D6, self.E5, self.F4, self.G7]

        self.G1.PossibleMoves = [self.D1, self.F2, self.G4]
        self.G4.PossibleMoves = [self.F4, self.G1, self.G7]
        self.G7.PossibleMoves = [self.D7, self.F6, self.G4]

        return [self.A1, self.A4, self.A7, self.B2, self.B4, self.B6, self.C3, self.C4, self.C5, self.D1, self.D2, self.D3, self.D5, self.D6, self.D7, self.E3, self.E4, self.E5, self.F2, self.F4, self.F6, self.G1, self.G4, self.G7]

    def allBoardMills(self):

        AA17 = [self.A1, self.A4, self.A7]
        BB26 = [self.B2, self.B4, self.B6]
        CC35 = [self.C3, self.C4, self.C5]
        DD13 = [self.D1, self.D2, self.D3]
        DD57 = [self.D5, self.D6, self.D7]
        EE35 = [self.E3, self.E4, self.E5]
        FF26 = [self.F2, self.F4, self.F6]
        GG17 = [self.G1, self.G4, self.G7]

        AG11 = [self.A1, self.D1, self.G1]
        BF22 = [self.B2, self.D2, self.F2]
        CE33 = [self.C3, self.D3, self.E3]
        AC44 = [self.A4, self.B4, self.C4]
        EG44 = [self.E4, self.F4, self.G4]
        CE55 = [self.C5, self.D5, self.E5]
        BF66 = [self.B6, self.D6, self.F6]
        AG77 = [self.A7, self.D7, self.G7]

        AC13 = [self.A1, self.B2, self.C3]
        CA57 = [self.C5, self.B6, self.A7]
        GE13 = [self.G1, self.F2, self.E3]
        EG57 = [self.E5, self.F6, self.G7]

        allBoardMills = [AA17, BB26, CC35, DD13, DD57, EE35, FF26, GG17, AG11, BF22, CE33, AC44, EG44, CE55, BF66, AG77, AC13, CA57, GE13, EG57 ]

        return allBoardMills


#    def getPlayerMove(avaiableBoard, player): 

class Game: 
    def __init__(self, player1, player2, board, turn):
        self.Player1 = player1
        self.Player2 = player2
        self.Board = board
        self.Turn = turn 
        self.Alternator = Game.alternate()
        self.CurrentPlayer = self.Player2

    def nextTurn(self):
        self.Turn = self.Alternator.__next__()
        if self.Turn == 1:
            self.Player2 = self.CurrentPlayer
            self.CurrentPlayer = self.Player1
        else:
            self.Player1 = self.CurrentPlayer
            self.CurrentPlayer = self.Player2
        self.Board = self.getCurrentBoard()

    def availableBoard(self):
        result = []
        for i in range(len(self.Board)):
            if self.Board[i].Symbol == ' ':
                result.append(self.Board[i])
        return result

    def findCow(pos, cows):
        for cow in cows:
            if cow.Pos == pos:
                return cow

    def exist(pos, cows):
        for cow in cows:
            if cow.Pos == pos: 
                return True
        return False 

    def filterOut(Cows, pos):
        return [cow for cow in Cows if cow.Pos != pos]

    def alternate():
        while True:
            yield 1
            yield 2

    def getCurrentBoard(self):
        cows = self.Player1.Cows + self.Player2.Cows  
        result = []
        for i in range(len(self.Board)):
            if Game.exist(self.Board[i].Pos, cows):
                result.append(Game.findCow(self.Board[i].Pos, cows))
            else:
                result.append(self.Board[i])
        return result 
    
    def checkIfMill(player, cow, allBoardMills):
        cows = player.Cows
        cows = cows.append(cow)
        for mill in allBoardMills:
            if exist(cow.pos, mill) & len(set(mill) & set(cows)) == 3:
                return True
        return False



