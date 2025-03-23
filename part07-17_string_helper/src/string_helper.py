from string import ascii_letters,digits,whitespace

def change_case(orig_string:str):
    new_word = ""
    for letter in orig_string:
        if letter.isupper() :
            new_letter = letter.lower()
        elif letter.islower() :
            new_letter = letter.upper()
        else :
            new_letter = letter
        new_word += new_letter 
    return new_word

def split_in_half(orig_string: str):
    return orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:]

def remove_special_characters(orig_string: str):
    allowed = ascii_letters + digits + whitespace
    modified = ""
    for l in orig_string :
        if l in allowed :
            modified += l
    return modified


if __name__ == "__main__":
    change_case("!!  TEST Number TwO22")
    split_in_half("abcdefg")
    remove_special_characters("hz21 !:^^ 5ello")