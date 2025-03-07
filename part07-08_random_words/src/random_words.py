from random import sample
def word_ref(file:str):
    w = []
    with open(file) as source :
        for line in source :
            w.append(line.strip())
    return w

def words(n: int, beginning: str):
    my_words = word_ref("words.txt")
    result = []
    for word in my_words :
        if word.startswith(beginning) :
            result.append(word)
    try :
        return sample(result,n)
    except :
        raise ValueError("Not enough words")
    
if __name__ == "__main__":
    word_list = words(8, "axw")
    for word in word_list:
        print(word)

