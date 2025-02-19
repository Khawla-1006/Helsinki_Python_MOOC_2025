# Write your solution here
def first_word(sentence) :
    i = 0 
    while i < len(sentence) :
        if sentence[i] == " " :
            break
        i += 1
    return(sentence[0 : i])


def second_word(sentence) :
    first = first_word(sentence)
    i = len(first) + 1
    while i < len(sentence) : 
        if sentence[i] == " " :
            break
        i += 1
    return(sentence[len(first) + 1 : i ])
    

def last_word(sentence) :
    i = -1
    while i >= -len(sentence) :
        if sentence[i] == " " :
            break
        i-=1
    return(sentence[i + 1 : ])
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))