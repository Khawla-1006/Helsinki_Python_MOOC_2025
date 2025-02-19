# Write your solution here
def play_turn(game_board : list , x :int, y : int, piece : str) :    
    if x <= 2 and x >= 0 and y <= 2 and y >= 0 :   
        if game_board[y][x] == "" :
            game_board[y][x] = piece
            return True
    return False

if __name__ == "__main__" :
    game_board = [['O', '', 'O'], ['', 'X', ''], ['X', 'O', '']]
    print(play_turn(game_board, 3, 0, "X"))
    print(game_board)