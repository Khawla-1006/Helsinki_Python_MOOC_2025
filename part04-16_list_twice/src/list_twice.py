# Write your solution here
my_list = []
while True :
    item = int(input("New item:"))
    if item == 0 :
        break
    my_list.append(item)
    print("The list now:",my_list)
    print("The list in order:",sorted(my_list))
print("Bye!")