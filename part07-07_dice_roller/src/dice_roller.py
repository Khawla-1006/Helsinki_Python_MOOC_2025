from random import choice
def roll(die: str):
    a = [3, 3, 3, 3, 3, 6]
    b = [2, 2, 2, 5, 5, 5]
    c = [1, 4, 4, 4, 4, 4]
    if die == "A":
        result = choice(a)
    elif die == "B":
        result = choice(b)
    elif die == "C":
        result = choice(c)
    return result

def  play(die1: str, die2: str, times: int):
    player1_won = 0
    player2_won = 0
    tie = 0
    for i in range(times):
        player1 = roll(die1)
        player2 = roll(die2)
        if player1 > player2 :
            player1_won += 1
        elif player2 > player1 :
            player2_won += 1
        elif player1 == player2:
            tie += 1
    return (player1_won,player2_won,tie)




if __name__ == "__main__":
    result = play("A", "B", 1000)
    print(result)
    result = play("B", "B", 100)
    print(result)