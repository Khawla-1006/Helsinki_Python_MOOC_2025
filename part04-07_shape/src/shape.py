# Copy here code of line function from previous exercise and use it in your solution
def line(number, string) : 
    if string == "" : 
        print("*" * number)
    else :
        print(string[0] * number)
def triangle(size, char) :
    i = 0 
    while i < size :
        i += 1
        line(i, char)

#final shape
def shape(width, char1, height, char2) : 
    triangle(width, char1)
    i = 0 
    while i < height :
        line(width, char2)
        i += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")