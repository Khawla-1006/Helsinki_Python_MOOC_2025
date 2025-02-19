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

def add_number(sudoku : list , row_no : int , column_no : int, number : int) :
    new_sudoku = sudoku[:]
    new_sudoku[row_no][column_no] = number
    return new_sudoku
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

    print_sudoku(sudoku)
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)