# Write your solution here
def no_shouting(string_list : list) : 
    no_shout = []
    for string in string_list :
        if str(string).isupper() == False :
            no_shout.append(string)
    return no_shout

if __name__ == "__main__" :
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)