# Write your solution here
def handle_file():
    lottery_numbers = {}
    with open("lottery_numbers.csv") as file :
        for line in file :
            d = line.strip().split(";")
            numbers = d[1].split(",")
            lottery_numbers[d[0]] = numbers
    return lottery_numbers

def test_int(number):
    try: 
        int(number)
        res = True
    except:
        res = False
    return res

def occurrence(my_list : list):
    occ = False
    for item in my_list :
        i = my_list.index(item)
        if item in my_list[i+1:]:
            occ = True
    return(occ)

def limit(list:list,lower: int,higher: int):
    test = True
    for number in list:
        try :
            if int(number) < lower or int(number) > higher :
                test = False
        except :
            return test

def filter_incorrect():
    source = handle_file()
    for key,value in source.items():
        key_test = key.split(" ")
        week_validation = test_int(key_test[1])
        occurrence_validation = occurrence(value)
        for num in value :
            integer_validation = test_int(num)
        if integer_validation == True :
            limit_validation = limit(value,1,39)
        else : 
            limit_validation = False
        if week_validation == True and integer_validation == True and occurrence_validation == True and limit_validation == True:
            with open("correct.csv","w") as correct :
                az = ""
                for ite in value:
                    az += int(ite) + ";"
                    az = az[:-1]
                correct.write(f"{key};{az}")

#DEBUG THIS SHIT!!

        




if __name__ == "__main__" :
    filter_incorrect()
    # l = handle_file()
    # print(l)
    # e = test_int('x3')
    # print(e)
