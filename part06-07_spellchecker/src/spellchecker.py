# write your solution here
to_check = input("Write text:")
with open("wordlist.txt") as content :
    reference =[]
    input_to_check = to_check.split(" ")
    for line in content :
        line = line.replace("\n","")
        reference.append(line)
    result = ""
    for item in input_to_check :
        if item.lower() not in reference :
            result += "*" + item + "* "
        else :
            result += item + " "
    print(result)