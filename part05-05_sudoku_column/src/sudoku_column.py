# Write your solution here
def column_correct(sudoku : list, column_no : int) :
    numbers = []
    for row in sudoku :
        if row[column_no] > 0 and row[column_no] in numbers :
            return False
        numbers.append(row[column_no])
    return True