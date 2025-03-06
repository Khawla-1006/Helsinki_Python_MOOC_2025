from fractions import Fraction
def fractionate(amount: int) :
    my_list = []
    while len(my_list) < amount :
        my_list.append(Fraction(1,amount))
    return my_list

if __name__ == "__main__" :
    test = fractionate(3)
    print(test)
    for p in fractionate(3):
       print(p)