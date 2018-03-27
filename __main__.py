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
    
def getPlayerMove(Game):
    return;  

def runGame(game)-> None:
   # printOut(game.board)
 #  getPlayerMove(game)
    
    #game.
    return
    

def main(): 
    
  #  player_1= Player("Player 1",'x',12,ThePlayerState.MOVING,[])
   # player_2= Player("Player 2",'o',12,ThePlayerState.MOVING,[])
  #  startBoard= Board()
    #print("Hi\n");
    #input("Enter something");
    row,col=getPos("Where do you want to move the cow?")
    print(row)
    print(col)
    return 
                         
    #Morabaraba= Game(player_1,player_2,startBoard,0);
    # runGame(Morabarba)
main()