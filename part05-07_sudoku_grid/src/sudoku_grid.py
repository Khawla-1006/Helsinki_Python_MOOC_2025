# Write your solution here
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True

def sudoku_grid_correct(sudoku: list) :
    for i in range(9) :
        check_row = row_correct(sudoku, i)
        check_col = column_correct(sudoku, i)
        if check_col == False or check_row == False :
            return False
    for j in range(6) :
        check_block = block_correct(sudoku, j , j)
        if check_block == False :
            return False
    return True