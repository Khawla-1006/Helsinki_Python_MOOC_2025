# Write your solution here
myList = [1 , 2 , 3 , 4 , 5]
while True :
    index = int(input("Index: "))
    if index == -1 :
        break
    new = int(input("New value: "))
    myList[index] = new
    print(myList)