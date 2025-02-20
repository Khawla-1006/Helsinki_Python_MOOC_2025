# write your solution here
def largest() :
    with open("numbers.txt") as numbers :
        large = 0
        for number in numbers :
            n = number.replace("\n","")
            if int(n) > large :
                large = int(n)
    return large

if __name__ == "__main__" :
    largest()