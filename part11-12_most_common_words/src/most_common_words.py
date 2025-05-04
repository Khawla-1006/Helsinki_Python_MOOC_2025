from string import punctuation
def most_common_words(filename: str, lower_limit: int):
    with open(filename) as file:
        #reding_the_file
        ref = file.read()
        #remove_punctuation
        no_punc = "".join([c for c in ref if c not in punctuation])
    
    refr = no_punc.split()
    return {word: refr.count(word) for word in refr if refr.count(word) >= lower_limit}

if __name__ == "__main__":
    print(most_common_words("comprehensions.txt", 3))
