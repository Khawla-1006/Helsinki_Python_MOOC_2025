# Write your solution here
def who_won(game_board : list) :
    player_one = 0
    player_two = 0
    empty = 0
    for row in game_board :
        for square in row :
            if square == 1 :
                player_one += 1
            elif square == 2 :
                player_two += 1
            else :
                empty += 1
    if player_one > player_two :
        return 1
    elif player_two > player_one :
        return 2
    else :
        return 0