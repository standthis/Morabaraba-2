import data
import os 

class colors():
    GREEN = '\033[32m' 
    ENDC = '\033[00m'
    RED = '\033[31m'

def printOut (game): 
    os.system('clear')
    print(' ' * 48, game.CurrentPlayer.Color + game.CurrentPlayer.Name + colors.ENDC)
    s = '''
                                    1   2   3       4      5   6   7
     
                                A  ({})-------------({})------------({})
                                    |\              |             /|
                                    | \             |            / |
                                    |  \            |           /  |
                                B   |  ({})---------({})--------({})  |          
                                    |   |\          |         /|   |          
                                    |   | \         |        / |   |         
                                    |   |  \        |       /  |   |        
                                C   |   |  ({})-----({})----({})  |   |     
                                    |   |   |              |   |   |
                                    |   |   |              |   |   |
                                D  ({})-({})-({})            ({})-({})-({})
                                    |   |   |              |   |   |          
                                    |   |   |              |   |   |       
                                E   |   |  ({})-----({})----({})  |   |   
                                    |   |  /        |       \  |   |     
                                    |   | /         |        \ |   |    
                                    |   |/          |         \|   |
                                F   |  ({})---------({})--------({})  |
                                    |  /            |           \  |
                                    | /             |            \ |
                                    |/              |             \|
                                G  ({})-------------({})------------({})
    '''

    print(s.format(*[cow.Symbol for cow in game.Board]))


cowSay = colors.GREEN + '''
                                                 ____________
                                                < Morabaraba-2 >
                                                 ------------
                                                       \   ,__,
                                                        \  (oo)____
                                                           (__)    )\\
                                                              ||--|| *
                                                               

                                               Press any key to play 
    ''' + colors.ENDC


