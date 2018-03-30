from data import * 
from board import printOut  

def main():
    player1 = Player("player1", 'X', 4, ThePlayerState.PLACING, [])
    player2 = Player("player2", 'O', 4, ThePlayerState.PLACING, [])
    board = Board()
    startboard = board.startBoard()
    allBoardMills = board.allBoardMills()
    game = Game(player1, player2, startboard, 1, allBoardMills)
    while True:
        runGame(game)


def getPos():
    row = input("What row: ")
    row = row[0].upper()

    col = input("What col: ")
    try:
        col = int(col)
    except:
        print("INCORRECT INPUT!") 
        getPos()
    return (row, col) 

def getPlayerMove(player, availableBoard, allBoardMills):
    while True:
        if player.PlayerState == ThePlayerState.PLACING:
            print("YOU ARE PLACING") 
            pos = getPos()
            if Game.exist(pos, availableBoard):
                player.addCow(Game.findCow(pos, availableBoard))
                return ('Z', 200) , pos
            else:
                print("You failed. Try again ")

        elif player.PlayerState == ThePlayerState.FLYING:
            print("YOU ARE FLYING") 
            print("Where do you want to move the cow from?: ")
            fromPos = getPos()
            if not Game.exist(fromPos, player.Cows):
                print("You have no cow there. Try again") 
            else : 
                print("Where do you want to move the cow to?: ")
                toPos = getPos()
                if Game.exist(toPos, availableBoard):
                    player.Cows = Game.filterOut(player.Cows, fromPos)
                    player.addCow(Game.findCow(toPos, availableBoard))
                    return fromPos, toPos
                else:
                    print("You can not move your cow there")
        else: 
            print("YOU ARE MOVING") 
            print("Where do you want to move the cow from?: ")
            fromPos = getPos()
            if not Game.exist(fromPos, player.Cows):
                print("You have no cow there. Try again") 
            else : 
                print("Where do you want to move the cow to?: ")
                toPos = getPos()
                if Game.exist(toPos, availableBoard):
                    if Game.exist(toPos, list(set(availableBoard) & 
                        set(Game.findCow(fromPos, player.Cows).PossibleMoves))):

                        player.Cows = Game.filterOut(player.Cows, fromPos)
                        player.addCow(Game.findCow(toPos, availableBoard))
                        return fromPos, toPos
                else:
                    print("You can not move your cow there")



def killCow(game):
    print("Which cow do you want to kill")
    pos = getPos()
    cowsInMill = sum(Game.getPlayerMills(game.OtherPlayer, game.AllBoardMills), [])
    if Game.exist(pos, list(set(game.OtherPlayer.Cows) - set(cowsInMill))):
        game.OtherPlayer.removeCow(Game.findCow(pos, game.OtherPlayer.Cows))
    else:
        print("invalid kill")
        killCow(game)

def checkStateChange(player):
    if (player.PlayerState == ThePlayerState.PLACING and
            player.UnplayedCows == 0):
        player.changePlayerState(ThePlayerState.MOVING)
    elif (player.PlayerState == ThePlayerState.MOVING and 
            len(player.Cows) == 3):
        player.changePlayerState(ThePlayerState.FLYING)

def runGame(game):
    game.nextTurn()
    checkStateChange(game.CurrentPlayer)
    print("Your turn: ", game.CurrentPlayer.Name)
    printOut(game.Board)
    fromPos, toPos = getPlayerMove(game.CurrentPlayer, game.availableBoard(), game.AllBoardMills)

    if Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills):
        killCow(game)
    checkStateChange(game.OtherPlayer)

main()

