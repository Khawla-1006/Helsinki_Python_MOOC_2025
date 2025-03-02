# Write your solution here
while True :
    print("1 - add an entry, 2 - read entries, 0 - quit")
    cmd = input("Function: ")
    if cmd == "0" :
        break
    elif cmd == "1" :
        diary_input = input("Diary entry:")
        print("Diary saved")
        with open("diary.txt", "a") as diary :
            diary.write(f"{diary_input}\n")
    elif cmd == "2" :
        print("Entries:")
        with open("diary.txt") as diary :
            for line in diary :
                output = line.replace("\n","")
                print(output)
print("Bye now!")