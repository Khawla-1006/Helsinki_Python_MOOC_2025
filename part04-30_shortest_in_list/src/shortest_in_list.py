# Write your solution here
def shortest(names: list):

    shortest_name = names[1]
    for name in names:
        if len(name) <= len(shortest_name):
          shortest_name = name
    return shortest_name

if __name__ == "__main__":
   my_list = ["first", "second", "fourth", "eleventh"]
   result = shortest(my_list)
   print(result)