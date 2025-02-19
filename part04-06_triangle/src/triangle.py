def line(number, string) : 
    if string == "" : 
        print("*" * number)
    else :
        print(string[0] * number)

def triangle(size):
    # You should call function line here with proper parameters
    i = 0 
    j = 1
    while i < size and j <= size :
        line(j, "#")
        i += 1
        j += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
