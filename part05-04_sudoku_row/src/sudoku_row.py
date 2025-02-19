# Write your solution here
def row_correct(sudoku : list , row_no : int) :
    occ = []
    for num in sudoku[row_no] :
        if num != 0 :
            occurrence = sudoku[row_no].count(num)
            occ.append(occurrence)
    for o in occ : 
        if o > 1 :
            return False
    return True

#another solution :
#def row_correct(sudoku: list, row_no: int):
    # numbers = []
    # for number in sudoku[row_no]:
    #     if number > 0 and number in numbers:
    #         return False
    #     numbers.append(number)
 
    # return True 