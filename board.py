class colors():
    GREEN = '\033[32m' 
    ENDC = '\033[00m'
    RED = '\033[31m'

def printOut (game): 
    morabarabaWord = '''
                        ___  ___                _                     _           
                        |  \/  |               | |                   | |          
                        | .  . | ___  _ __ __ _| |__   __ _ _ __ __ _| |__   __ _ 
                        | |\/| |/ _ \| '__/ _` | '_ \ / _` | '__/ _` | '_ \ / _` |
                        | |  | | (_) | | | (_| | |_) | (_| | | | (_| | |_) | (_| |
                        \_|  |_/\___/|_|  \__,_|_.__/ \__,_|_|  \__,_|_.__/ \__,_|

    '''
    print('\n' * 5, morabarabaWord)
    print(' ' * 34, 'PLAYER 1:', '\t' * 2, 'PLAYER 2:')
    print(' ' * 34, '---------', '\t' * 2, '---------')
    print(' ' * 34, 'Unplaced Cows: ', game.Player1.UnplayedCows, '\t', 'Unplaced Cows: ', game.Player2.UnplayedCows)
    print(' ' * 34, 'Cows Alive: ', len(game.Player1.Cows),'\t', 'Cows Alive: ', len(game.Player2.Cows))
    print(' ' * 34, 'Cows Killed: ', (12 - game.Player2.UnplayedCows - len(game.Player2.Cows)), '\t', 'Cows Killed: ', (12 - game.Player1.UnplayedCows - len(game.Player1.Cows)))
    print('\n',' ' * 43, game.CurrentPlayer.Name + '\'s turn')
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
                                                               

                                               Press ENTER to play 
    ''' + colors.ENDC