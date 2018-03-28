import data
def printOut (board:data.Game): 
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

