# Write your solution here
def most_common_character(my_str : str) :

    max_char_occ = my_str[0]
    max_occ = 1
    for char in my_str : 
        occ = my_str.count(char)
        if occ > max_occ :
            max_occ = occ
            max_char_occ = char
    return max_char_occ

if __name__ == "__main__" :
    first_string = "abcdbde"
    print(most_common_character(first_string))
    
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))