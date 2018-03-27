#import data 
import board

from data import *



def getPos(what:str):
    print(what)
    row=input("Row: ").upper()
    try:                        #try for exception incase user enters space
        row=row[0];
    except IndexError:
        print("Please enter a character for the row!")
        return getPos(what)
    try:
        col=int(input("Column: "))
    except ValueError:
        print("\nPlease enter a int for a column!")
        return getPos(what)
    return (row,col);  
    
def getPlayerMove(game:Game):    
    if(game.turn==0):       #player 1's turn
      player= game.Player1
    else:                   #player 2's turn
      player= game.Player2
     
    if(player.PlayerState==ThePlayerState.MOVING):
        
        toRow,toCol=getPos("{0}'s turn\nWhere do you want to place the cow?".format(player.Name));
        
        #if(game.isValidPlace((row,col))): //check if the positions is in the available board
            #make placeholder from  and to pos's
            fromRow='Z'
            fromCol=100;
            # return (fromRow,toCol),(toRow,toCol)
        else:
            printf("Can't move cow to ({0},{1}})".format(toRow,toCol))
            getPlayerMove(game,player)
                         
    elif(player.PlayerState==ThePlayerState.PLACING or player.PlayerState==ThePlayerState.FLYING):
        
         fromRow,fromCol=getPos("{0}'s turn\nWhere do you want movethe cow from?".format(player.Name))
        
       #  if(game.isValidFrom(player,(fromRow,fromCol))): //check if player has postion (fromRow,fromCol)
              toRow,toCol=getPos("{0}'s turn\nWhere do you want move the cow to?".format(player.Name))
         #     if(game.isValidTo(player,(toRow,toCol))): //check if player can move to that available board checking their state too
               # return (fromRow,toCol),(toRow,toCol) 
              else:
                 printf("Can't move from ({0},{1})cow to ({2},{3})".format(fromRow,fromCol,toRow,toCol))
                 #return getPlayerMove(game,player)
                  
         else:
            printf("You have now cow at ({0},{1}}".format(fromRow,fromCol))
           #return getPlayerMove(game,player)
               
            
      
  
  
 #   print("User wants to move to ({0},{1})".format(row, col))
    #return newGame,newPlayer if we can't pass by reference
    #return;  



def runGame(game:Game)-> None:

    board.printOut(game.Board)
    fromPos, toPos= getPlayerMove(game)
    #game.updatePlayer((fromRow,fromCol),(toRow,toCol));  //update the board and player positions based on the players state
                                  #game will know who's turn it is and will return the appropriate player
    #if(game.checkFromMills()):  //check if a board mills was formed by the current play
       #killRow,killCol=killCow(game)
       #game.killCow((row,col));
     #if(game.checkEnd()): //game should check if enemy player is not moving and that enemy player has more than 2 cows (IF FLYING)
     # game.end() //prints out the appropriate ending message  
     #else    
     #    game.changePlayerTurn() 
     #    runGame(game)
  
    

                               
    

def main():
player_1= Player("Player 1",'x',12,ThePlayerState.MOVING,[])
player_2= Player("Player 2",'o',12,ThePlayerState.MOVING,[])
startBoard= Board()
game= Game(player_1,player_2,startBoard,0);  
runGame(game,game.Player1,game.Player2);                  
    return 

                
main()