# Name:Lynn Mumia
# Section:2
# nims.py


def check_if_valid(ans,max_number,pile_left):
    '''
    Checks if a player answer is valid
    @param ans : the answer of the active player
    @param max_number : the maximum number of stones you can take on one turn
    @param pile_left : amout of stones in the pile left
    @return True : if player answer is valid
    '''
    if (ans > 0):
        if (ans <= max_number):
            checker = pile_left - ans
            if checker >= 0:
                return True
    return False


def play_nims(pile, max_stones):
    
    '''
    An interactive two-person game; also known as Stones.
    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''   
   
    winner=0
    while (pile > 0):
        player1=0
        while not check_if_valid(player1,max_stones,pile):
            print ("player 1 turn:")
            player1=int(input("Enter a number between 1-" + str(max_stones)))                                  
        print "Player 1 stones : " + str(player1)
                
        pile = pile-player1
        if(pile==0):
           winner=1
           break
            
        player2=0
        while not check_if_valid(player2,max_stones,pile):
            print ("player 2 turn:")
            player2=int(input("Enter a number between 1 -"  + str(max_stones)))
        print "Player 2 stones : " + str(player2)
                        
        pile = pile-player2             
        if(pile==0):
           winner=2
               
    print ("Congratulations Winner is player " + str(winner))
    print ("Game over")
        
if __name__=="__main__":
    pile=100
    play_nims(pile,5)
    
