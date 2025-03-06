from random import sample
def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower,upper))
    result = sorted(sample(number_pool,amount))
    return result

if __name__ == "__main__" :
    test = lottery_numbers(7,45,101)
    print(test)
    