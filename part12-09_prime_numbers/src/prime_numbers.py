# Write your solution here
def test_prime(x:int):
    if x < 2:
        return False
    
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
def prime_numbers():
    number = 2
    while True :
        if test_prime(number):
            yield number
        number += 1

if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))