# import math

def average(my_dict:dict):
    val = []
    for value in my_dict.values():
        if type(value) == str :
            continue
        val.append(value)
    av = sum(val)/ len(val)
    return av

def smallest_average(person1:dict,person2:dict,person3:dict):
    persons = [person1,person2,person3] 
    smallest = person1
    for person in persons :
        if average(person) < average(smallest) :
            smallest = person
    return smallest


if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average({"result1": 4,"result2": 3,"result3": 4}, {"result1": 4,"result2": 2,"result3": 4}, {"result1": 4,"result2": 3,"result3": 4}))