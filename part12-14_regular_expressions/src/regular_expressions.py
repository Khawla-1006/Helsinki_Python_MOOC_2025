# Write your solution here
import re
def is_dotw(my_string: str):
    days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
    for day in days :
        if re.search(day, my_string):
            return True
    return False

def all_vowels(my_string: str):
    if re.search("^[aeiou]*$",my_string):
        return True
    return False
    
def time_of_day(my_string: str):
    if re.search("^(0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$",my_string):
        return True
    return False




if __name__ == "__main__":
    print(is_dotw("Mon"))
    print(is_dotw("Fri"))
    print(is_dotw("Tui"))
    print(all_vowels("eioueioieoieou"))
    print(all_vowels("autoooo"))
    print(time_of_day("12:43:01"))
    print(time_of_day("AB:01:CD"))
    print(time_of_day("17:59:59"))
    print(time_of_day("33:66:77"))