# # There’s a game, “takeaway”, that is played by two players, using a number of stones.

# # The first player goes first. She can take 2, 3, or 5 stones from the pool. The second player goes next; she can also remove 2, 3, or 5 stones. The first player then goes, and so on.

# # If a player is unable to move (there are fewer than 2 stones), they lose.

# Imagine that both players have “perfect play” — that is, they always make the best possible move. Then, you can absolutely determine who would win a game with n stones.

# >>> can_win(1)
# False

# >>> can_win(2)
# True

# >>> can_win(7) 2 - 5
#False 

# >>> can_win(9) 2 - 5 - 2 / 3 - 5 / 5 - 3 
#True

#can_win(2) => return True
#can_win(9-2) => False
#can_win(7-5)
# => return True
#1
#Player #1 cannot move, so player #2 win

#2
#Player #1 takes 2 stones, and player #2 cannot move

#can_win(x) x = num of given stones
#True is if Player 1 wins, False if not 
#Player 1 wins if they're the last to get stones

#define function that takes in num of stones as int
def can_win(stones):

#variable to keep track of whose turn it i
#player_1 = True
    options = [5, 3, 2]

    if stones < 2: 
        return False
#if stones == 2, return True
    if stones == 2:
        return True 

    #loop over options, if the other player can't choose any of them, we've won this round
    for option in options:
        if not can_win(stones - option):
            return True
    
    return False
