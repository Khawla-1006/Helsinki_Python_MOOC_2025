# Write your solution here
def even_numbers(number_list : list) :
    even = []
    for number in number_list :
        if number % 2 == 0 :
            even.append(number)
    return even

if __name__ == "__main__" :
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)