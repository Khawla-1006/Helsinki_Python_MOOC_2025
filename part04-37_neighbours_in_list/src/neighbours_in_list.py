# Write your solution here
def longest_series_of_neighbours(my_list : list) :
    series = 1
    max_len=0
    for i in range(len(my_list) - 1) :
        if abs(my_list[i] - my_list[i+1]) == 1 :
            series += 1
        else :
            series = 1
        if series >= max_len : 
            max_len = series
        
    return max_len

if __name__ == "__main__" :
    my_list = [1, 2, 5, 7, 6, 5, 6,5,4, 3, 4, 1, 0]
    print(longest_series_of_neighbours(my_list))
