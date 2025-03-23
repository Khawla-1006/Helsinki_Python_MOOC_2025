import difflib

def reference():
    words = []
    with open("wordlist.txt") as source :
        for line in source :
            line = line.strip()
            words.append(line)
    return words

user_input = input("write text: ")
ref = reference()
words_to_check = user_input.split(" ")
output = ""
misspelled = []
for word in words_to_check :
    if word.lower() not in ref :
        misspelled.append(word)
        word = f"*{word}*"
    output += word + " "
print(output)
print("suggestions:")
for m in misspelled :
    correct = ""
    suggestions = difflib.get_close_matches(m,ref)
    correct = ",".join(suggestions)
    print(f"{m}: {correct}")


