# Write your solution here
integer = int(input("Please type in a positive integer:"))
for i in range(-integer , integer + 1) :
    if i == 0 :
        continue
    print(i)