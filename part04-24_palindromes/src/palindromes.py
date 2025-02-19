# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes(string : str):
    reversed_string = string[::-1]
    if reversed_string == string :
        return True
    return False


while True :
    input_string = input("Please type in a palindrome:")
    if palindromes(input_string) : 
        break
    else :
        print("that wasn't a palindrome")
print(input_string,"is a palindrome!")



# another solution
def is_palindrome(word : str) :
    for i in range(len(word)//2):
        if word[i] != word[len(word) - i - 1]:
            return False
    return True