# Write your solution here
def new_person(name:str,age:int):
    test = name.split(" ")
    if name == "":
        raise ValueError("Name is an empty string") 
    elif len(test) < 2 :
        raise ValueError("Name contains less than two words")
    elif len(name) > 40 :
        raise ValueError("Name is longer than 40 characters")
    elif age < 0 :
        raise ValueError("age is a negative number")
    elif age > 150 :
        raise ValueError("age is greater than 150")
    else:
        return (name,age)
    
#MODEL_SOLUTION:
def new_person2(name : str , age : int):
    #validate name
    if name =="" or (" "not in name) or len(name) > 40 :
        raise ValueError("Invalid argument value for name: " + name)
    #validate age
    if age < 0 or age > 150 :
        raise ValueError("Invalid argument value for age: "+ str(age))
    return(name,age) 

# new_person("khawla",254)
# new_person2("kh ali",-9)