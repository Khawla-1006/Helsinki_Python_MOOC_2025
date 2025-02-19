# Write your solution here
phone_book = {}

while True :
    c = int(input("command (1 search, 2 add, 3 quit):"))
    if c == 3 :
        break
    elif c == 2 : 
        numbers = []
        input_name = input("name:")
        input_number = input("number:")
        print("ok!")
        if input_name in phone_book.keys():
            phone_book[input_name].append(input_number)
        else :
            numbers.append(input_number)
            phone_book[input_name] = numbers    
    elif c == 1 :
        searched_name = input("name:")
        if searched_name not in phone_book :
            print("no number")
        else :
            for num in phone_book[searched_name]:
                print(f"{num}")
print("quitting...")



#better solution 
# def search(persons):
#     name = input("name: ")
#     if name in persons:
#         for number in persons[name]:
#             print(number)
#     else:
#         print("no number")
 
# def add(persons):
#     name = input("name: ")
#     number = input("number: ")
#     if name not in persons:
#         persons[name] = []
#     persons[name].append(number)
#     print("ok!")
 
# def main():
#     persons = {}
#     while True:
#         cmd = input("command (1 search, 2 add, 3 quit): ")
#         if cmd == "1":
#             search(persons)
#         if cmd == "2":
#             add(persons)
#         if cmd == "3":
#             break
#     print("quitting...")
 
# main()