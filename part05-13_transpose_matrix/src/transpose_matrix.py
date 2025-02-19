# Write your solution here
def transpose(matrix : list) :
    copy = []
    for row in matrix :
        copy_row = row[:]
        copy.append(copy_row)
    for j in range(len(copy)) :
        for i in range(len(matrix[j])) :
            matrix[i][j] = copy[j][i]

if __name__ == "__main__" :
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    transpose(matrix)
