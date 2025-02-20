# write your solution here
def read_fruits() :
    fruit_dict = {}
    with open("fruits.csv") as fruit_file :
        for fruit in fruit_file :
            fruit = fruit.replace("\n","")
            line = fruit.split(";")
            name = line[0]
            price = float(line[1])
            fruit_dict[name] = price
    return fruit_dict