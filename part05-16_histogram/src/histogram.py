# Write your solution here
def histogram(string : str) :
    d = {}
    for letter in string :
        if letter not in d :
            d[letter] = ""
        d[letter] += "*"
    
    for key , value in d.items():
        print(f"{key} {value}")