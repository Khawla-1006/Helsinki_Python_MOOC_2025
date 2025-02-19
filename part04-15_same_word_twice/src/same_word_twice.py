# Write your solution here
my_words = []

while True :
    word = input("Word: ")
    if word in my_words :
        break
    my_words.append(word)
print("You typed in", len(my_words),"different words")
