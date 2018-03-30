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

                #getPlayerMove(player, availableBoard, allBoardMills)

        elif player.PlayerState == ThePlayerState.FLYING:
            print("YOU ARE FLYING") 
            print("Where do you want to move the cow from?: ")
            fromPos = getPos()
            if not Game.exist(fromPos, player.Cows):
                print("You have no cow there. Try again") 
                #getPlayerMove(player, availableBoard, allBoardMills)
            else : 
                print("Where do you want to move the cow to?: ")
                toPos = getPos()
                if Game.exist(toPos, availableBoard):
                    player.Cows = Game.filterOut(player.Cows, fromPos)
                    player.addCow(Game.findCow(toPos, availableBoard))
                    return fromPos, toPos
                else:
                    print("You can not move your cow there")
                    #getPlayerMove(player,availableBoard, allBoardMills)
        else: 
            print("YOU ARE MOVING") 
            print("Where do you want to move the cow from?: ")
            fromPos = getPos()
            if not Game.exist(fromPos, player.Cows):
                print("You have no cow there. Try again") 
                #getPlayerMove(player, availableBoard, allBoardMills)
            else : 
                print("Where do you want to move the cow to?: ")
                toPos = getPos()
                #if Game.exist(toPos, list((set(availableBoard) & 
                #    set(Game.findCow(toPos, availableBoard).PossibleMoves)))):
                if Game.exist(toPos, availableBoard):
                    if Game.exist(toPos, list(set(availableBoard) & 
                        set(Game.findCow(fromPos, player.Cows).PossibleMoves))):

                        player.Cows = Game.filterOut(player.Cows, fromPos)
                        player.addCow(Game.findCow(toPos, availableBoard))
                        return fromPos, toPos
                else:
                    print("You can not move your cow there")
                    #getPlayerMove(player,availableBoard, allBoardMills)



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
    print("HERE!!!")
    print(Game.findCow(toPos, game.CurrentPlayer.Cows).PossibleMoves)
    # Testing for fromPos, toPos as they are causing an error 
    print("FROMPOS is NONE -> ", fromPos is None, "TOPOS is NONE  -> ", toPos is None)
    if fromPos is not None and toPos is not None:
        print("FROMPOS -> ", fromPos, "TOPOS -> ", toPos)

    if Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills):
        killCow(game)
   # availPos = list((set(game.availableBoard()) & set(Game.findCow(toPos, game.availableBoard()).PossibleMoves)))
   # print("SETS DEBUG")
   # print("--------------------")
   # for a in availPos:
   #     print(a.Pos)

main()

