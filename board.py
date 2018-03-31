import data

class colors():
    GREEN = '\033[32m' 
    ENDC = '\033[00m'
    RED = '\033[31m'

def printOut (board): 
    boardToPrint=[]
    for element in board:
        boardToPrint.append(element.Symbol)
    
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

    print(s.format(*boardToPrint))


cowSay = colors.GREEN + '''
                                                 ____________
                                                < Morabaraba-2 >
                                                 ------------
                                                       \   ,__,
                                                        \  (oo)____
                                                           (__)    )\\
                                                              ||--|| *
                                                               

                                               Press any key to coninue 
    ''' + colors.ENDC


