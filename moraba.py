from data import * 
from board import printOut, cowSay, colors   

def localMain():
    player1 = Player("Player 1", 'X', 12, ThePlayerState.PLACING, [], colors.GREEN, 0)
    player2 = Player("Player 2", 'O', 12, ThePlayerState.PLACING, [], colors.RED, 1)
    board = Board()
    startboard = board.startBoard()
    allBoardMills = board.allBoardMills()
    game = Game(player1, player2, startboard, 1, allBoardMills)
    
    print(cowSay)
    input()
    
    while not game.endGame(): 
        runGame(game)

def getPos():
    row = input("What row: ")
    try:
        row = row[0].upper()
    except: 
        print("INCORRECT INPUT!") 
        return getPos()

    col = input("What col: ")
    try:
        col = int(col)
    except:
        print("INCORRECT INPUT!") 
        return getPos()
    
    return (row, col) 

def getPlayerMove(player, availableBoard, allBoardMills):
    while True:
        if player.PlayerState == ThePlayerState.PLACING:
            print("YOU ARE PLACING") 
            pos = getPos()
            
            if Game.exist(pos, availableBoard):
                player.addCow(Game.findCow(pos, availableBoard))
                return ('Z', 2), pos
            else:
                print("You failed. Try again")

        elif player.PlayerState == ThePlayerState.FLYING:
            print("YOU ARE FLYING") 
            print("Where do you want to move the cow from?: ")
            fromPos = getPos()
            
            if not Game.exist(fromPos, player.Cows):
                print("You have no cow there. Try again") 
                
            else: 
                print("Where do you want to move the cow to?: ")
                toPos = getPos()
                
                if Game.exist(toPos, availableBoard):
                    player.removeCow(Game.findCow(fromPos, player.Cows))
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
                
            else: 
                print("Where do you want to move the cow to?: ")
                toPos = getPos()
                
                if Game.exist(toPos, list(set(availableBoard) & 
                    set(Game.findCow(fromPos, player.Cows).PossibleMoves))):
                    player.removeCow(Game.findCow(fromPos,player.Cows))
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
        return pos
    elif len(game.OtherPlayer.Cows) == len(cowsInMill):
        if Game.exist(pos,game.OtherPlayer.Cows):
            game.OtherPlayer.removeCow(Game.findCow(pos, game.OtherPlayer.Cows))
            return pos
        else:
            print("invalid kill")
            return killCow(game)
    else:
        print("invalid kill")
        return killCow(game)
    
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
    printOut(game)
    fromPos, toPos = getPlayerMove(game.CurrentPlayer, game.availableBoard(), game.AllBoardMills)

    if Game.checkIfMill(game.CurrentPlayer, Game.findCow(toPos, game.Board), game.AllBoardMills):
        printOut(game)
        killCow(game)
        
    checkStateChange(game.OtherPlayer)
