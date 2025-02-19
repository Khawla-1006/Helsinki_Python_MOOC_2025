# Write your solution here
list = []
i = 1
x = int(input("How many items: "))
while i <= x :
    item = int(input(f"Item {i}:"))
    list.append(item)
    i += 1
print(list)