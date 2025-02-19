# Write your solution here
# Write your solution here
def factorials(n : int) :
    d = {}
    for i in range(1 ,n + 1) :
        fact = 1
        j = 1
        while j <= i:
            fact *= j 
            j += 1
        d[i] = fact
    return d

#another solution
def factorials_2(n: int):
    result = {}
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i-1] * i
    return result

if __name__ == "__main__" :
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])
