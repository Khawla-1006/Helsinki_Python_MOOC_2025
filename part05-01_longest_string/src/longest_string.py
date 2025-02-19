# Write your solution here
def longest(strings : list) :
    long_string = strings[0]
    for string in strings :
        if len(string) > len(long_string) :
            long_string = string
    return long_string