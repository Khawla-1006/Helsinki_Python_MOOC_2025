# Write your solution here
def everything_reversed(my_list : list) :
    reversed_list = []
    for item in my_list :
        new_item = item[::-1]
        reversed_list.append(new_item)
    reversed_list = reversed_list[::-1]
    return reversed_list

if __name__ == "__main__" :
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)  