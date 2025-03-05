# Write your solution here
def read_input(message:str,lower,higher):
    while True :
        try :
            str_input = input(message)
            number = int(str_input)
            if number > lower and number < higher:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lower} and {higher}")
if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)