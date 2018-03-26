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

def startBoard():
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

