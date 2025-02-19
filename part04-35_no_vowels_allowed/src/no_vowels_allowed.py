# Write your solution here
def no_vowels(my_string : str) :
    for vowel in ["a","e","o","i","u"]: 
        no_vowel_string = my_string.replace(vowel,"")
        my_string = no_vowel_string
    return my_string
             
        
if __name__ == "__main__" :
    my_string = "abcdefghijklmnopqrstuvwxyz"
    print(no_vowels(my_string))