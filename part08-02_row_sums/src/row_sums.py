def row_sums(my_matrix: list):
    for li in my_matrix:
        li.append(sum(li))

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)