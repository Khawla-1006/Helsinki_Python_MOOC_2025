from datetime import datetime

def validate_date(date : str, marker : str):
    test_date = True
    if marker == "-" :
        c = "18"
    elif marker == "+":
        c = "19"
    elif marker =="A":
        c = "20"
    new_date = date[:4]+ c +date[4:6]    
    try :
        user_input = datetime.strptime(new_date,"%d%m%Y")
    except ValueError:
        test_date = False
        # print("date is not valid")
    return test_date

def validate_marker(marker : str):
    test_marker = False
    if marker in {"+","-","A"}:
        test_marker = True
    return test_marker

def control_char(date:str , pid : str,z:str):
    c_char = False
    full_str = date + pid
    index = int(full_str) % 31
    ref = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if ref[index] == z :
        c_char = True
    return c_char


def is_it_valid(pic:str):
    date = pic[:6]
    marker = pic[6:7]
    pid = pic[7:10]
    z = pic[10:]
    date_test = False
    marker_test = validate_marker(marker)
    if marker_test == True :
        date_test = validate_date(date,marker)
    control_character_test = control_char(date,pid,z)

    if marker_test == True and date_test == True and control_character_test == True :
        valid = True
        # print("PIC is valid")
    else :
        valid = False
        # print("PIC is not valid")

    return valid

if __name__ == "__main__":
    is_it_valid("230827-906F")