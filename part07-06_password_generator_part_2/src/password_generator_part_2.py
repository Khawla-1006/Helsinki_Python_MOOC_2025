from string import ascii_lowercase
from random import sample,randint,choice
def generate_strong_password(length : int,cnd_1: bool,cnd_2:bool) :
    password = ""
    h = []
    n = []
    for c in ascii_lowercase :
        h.append(c)
    for i in range(0,10):
        n.append(str(i))
    if cnd_1 == True :
        p = str(choice(ascii_lowercase)) + str(randint(0,9)) #at least one number
        password += p
        chars = sample(h+n,length)
    if cnd_2 == True :
        p = str(choice(ascii_lowercase)) + str(choice(["!","?","=","+","-","(",")","#"])) #at least one special char
        password += p
        chars = sample(["!","?","=","+","-","(",")","#"]+h,length)
    if cnd_1 == False and cnd_2==False :
        chars = sample(ascii_lowercase,length)
    if length == 2 :
        chars = [choice(["!","?","=","+","-","(",")","#"])]+[str(randint(0,9))]
    for char in chars :
        if len(password) < length :
            password += char
    return password



    
if __name__ == "__main__":
    test = generate_strong_password(5,True,True)
    print(test)
    for i in range(10):
        print(generate_strong_password(5,True,True))
    
