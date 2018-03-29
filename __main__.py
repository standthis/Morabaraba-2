from data import * 
from board import printOut  

def main():
    player1 = Player("player1", 'X', 12, ThePlayerState.PLACING, [])
    player2 = Player("player2", 'O', 12, ThePlayerState.PLACING, [])
    board = Board()
    startboard = board.startBoard()
    allBoardMills = board.allBoardMills()
    game = Game(player1, player2, startboard, 1, allBoardMills)
    while True:
        runGame(game)


def getPos():
    row = input("What row: ")
    row = row.upper()
    col = int(input("What col: "))
    return (row, col) 

def getPlayerMove(player, availableBoard, allBoardMills):
    if player.PlayerState == ThePlayerState.PLACING:
        pos = getPos()
        if Game.exist(pos, availableBoard):
            player.addCow(Game.findCow(pos, availableBoard))
            return ('Z', 200) , pos
        else:
            print("You failed. Try again ")
            getPlayerMove(player, availableBoard, allBoardMills)

    else:
        print("Where do you want to move the cow from?: ")
        fromPos = getPos()
        if not Game.exist(fromPos, player.Cows):
            print("You have no cow there. Try again") 
            getPlayerMove(player, availableBoard, allBoardMills)
        else : 
            print("Where do you want to move the cow to?: ")
            toPos = getPos()
            if Game.exist(toPos, availableBoard):
                player.Cows = Game.filterOut(player.Cows, fromPos)
                player.addCow(Game.findCow(toPos, availableBoard))
            else:
                print("You can not move your cow there")
                getPlayerMove(player,availableBoard, allBoardMills)


def killCow(game):
    print("Which cow do you want to kill")
    pos = getPos()
    cowsInMill = sum(Game.getPlayerMills(game.OtherPlayer, game.AllBoardMills), [])
    if Game.exist(pos, list(set(game.OtherPlayer.Cows) - set(cowsInMill))):
        game.OtherPlayer.removeCow(Game.findCow(pos, game.OtherPlayer.Cows))
    else:
        print("invalid kill")
        killCow(game)



def runGame(game):
    game.nextTurn()
    game.checkStateChange()
    print(game.CurrentPlayer.Name)
    printOut(game.Board)
    fromPos, toPos = getPlayerMove(game.CurrentPlayer, game.availableBoard(), game.AllBoardMills)
    if Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills):
        killCow(game)

main()

