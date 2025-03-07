from string import ascii_lowercase
from random import sample
def generate_password(length : int) :
    password = ""
    chars = sample(ascii_lowercase,length)
    for char in chars :
        password += char
    return password
    
if __name__ == "__main__":
    test = generate_password(8)
    print(test)
    for i in range(10):
        print(generate_password(8))