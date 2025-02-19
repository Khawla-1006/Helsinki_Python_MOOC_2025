# Write your solution here
def spruce(x) : 
    print("a spruce!")
    i = x 
    while i > 0 :
        print(" " * (i - 1) + "*" * (x - i + 1) + "*" * (x - i))
        i -= 1
    print(" " * (x - 1) + "*")
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)