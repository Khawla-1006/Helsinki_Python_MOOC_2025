# Write your solution here
def block_correct(sudoku : list , row_no : int, column_no : int) :
    numbers = []
    for row in sudoku[row_no : row_no + 3] :
        for col in row[column_no : column_no + 3] :
            if col > 0 and col in numbers :
                return False 
            numbers.append(col)
    return True