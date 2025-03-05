# A GOOD PRACTICE : save the content of the txt file aside 
with open("dictionary.txt") as file :
    content =[]
    for line in file :
        content.append(line.strip())
# print(content)

with open("dictionary.txt","a") as file :
    while True :
        print("1 - Add word, 2 - Search, 3 - Quit")
        cmd = input("Function: ")
        if cmd == "1" :
            word = input("The word in Finnish: ")
            traduction = input("The word in English: ")
            file.write(f"{word} - {traduction}\n")
            content.append(f"{word} - {traduction}")
            print("Dictionary entry added")
        if cmd == "2":
            search = input("Search term: ")
            for item in content :
                # print(item)
                if search in item :
                    print(item)

        if cmd == "3" :
            print("Bye!")
            break
