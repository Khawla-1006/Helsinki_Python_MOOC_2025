# Write your solution here
def all_the_longest(my_list : list):
    all = []
    longest = max(my_list,key=len)
    for item in my_list :
        if len(item) == len(longest):
            all.append(item)
    return all


if __name__ == "__main__" :
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = all_the_longest(my_list)
    print(result)