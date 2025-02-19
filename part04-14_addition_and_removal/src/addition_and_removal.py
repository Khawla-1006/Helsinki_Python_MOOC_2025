# Write your solution here
list = []
i = 0
j = 1 
while True :
    print("The list is now", list)
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d" : 
        if list == [] :
            i = 0 
            j = 1
        list.insert(i, j)
        i += 1 
        j += 1
    elif choice == "r" :
        list.pop(len(list) - 1)
        j = len(list) + 1
    elif choice == "x" :
        break
print("Bye!")    