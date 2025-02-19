# Write your solution here
def print_sudoku(sudoku: list):
    for j in range(len(sudoku)) :
        for i in range(len(sudoku[j])) :
            if i == 3 or i == 6 :
                if sudoku[j][i] > 0 :
                    print(f" {sudoku[j][i]}", end=" ")         
                else : 
                    print(" _", end=" ")
            else :
                if sudoku[j][i] > 0 :
                    print(f"{sudoku[j][i]}", end=" ")         
                else :
                    print("_", end=" ")
        if j == 2 or j == 5 :
            print()
            print()
        else :
            print()

def copy_and_add(sudoku : list , row_no : int , column_no : int, number : int) :
    new_su = []
    for row in sudoku :
        row_copy = row[:]
        new_su.append(row_copy)
    new_su[row_no][column_no] = number
    return new_su



if __name__ == "__main__" :

    sudoku  = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)