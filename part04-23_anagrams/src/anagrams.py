# Write your solution here
def anagrams(string1 , string2):
    sorted_string1 = sorted(list(string1))
    # print(sorted_string1)
    sorted_string2 = sorted(list(string2))
    # print(sorted_string2)
    if sorted_string1 == sorted_string2 :
        return True
    else :
        return False

if __name__ == "__main__":
    anagrams("house", "mouse")