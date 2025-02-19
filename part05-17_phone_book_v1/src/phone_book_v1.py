# Write your solution here
phone_book = {}
while True :
    c = int(input("command (1 search, 2 add, 3 quit):"))
    if c == 3 :
        break
    elif c == 2 :
        input_name = input("name:")
        input_number = input("number:")
        print("ok!")
        phone_book[input_name] = input_number
    elif c == 1 :
        searched_name = input("name:")
        if searched_name not in phone_book :
            print("no number")
        else :
            print(f"{phone_book[searched_name]}")
print("quitting...")
    