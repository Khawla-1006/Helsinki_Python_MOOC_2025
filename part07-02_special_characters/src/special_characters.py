# Write your solution here
from string import ascii_letters,punctuation
# print(dir(string))
def separate_characters(my_string: str) :
    shit = ""
    p =""
    r =""
    for char in my_string :
        if char in ascii_letters :
            shit += char
        elif char in punctuation :
            p += char
        else :
            r += char
    return(shit,p,r)

if __name__ == "__main__":
    parts =separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])