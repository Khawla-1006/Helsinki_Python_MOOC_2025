# Write your solution here
def filter_solutions():
    solutions_data = []
    with open("solutions.csv") as solutions :
        for line in solutions :
            n = line.strip().split(";")
            solutions_data.append(n)
    correct = []
    incorrect = []
    for data in solutions_data :
        if eval(data[1]) == int(data[2]):
            correct.append(data)
        else :
            incorrect.append(data)
    with open("correct.csv", "w") as correct_answers:
        for answer in correct :
            line = ""
            for value in answer :
                line += f"{value};"
            line = line[:-1]
            correct_answers.write(line+"\n")
    with open("incorrect.csv", "w") as incorrect_answers :
        for ans in incorrect :
            line = ""
            for val in ans :
                line += f"{val};"
            line = line[:-1]
            incorrect_answers.write(line+"\n")

########### MODEL SOLUTION ############

def filter_sol():
    #open all files 
    with open("solutions.csv") as source, open("corrects.csv", "w")as correct_file, open("incorrects", "w") as incorrect_file :
        for row in source :
            pieces = row.split(";")
            calculations = pieces[1]
            results = pieces[2]
        #addition or substraction ?
        if "+" in calculations :
            operands = calculations.split("+")
            correct = int(operands[0]) + int(operands[1]) == int(results) #correct is true or false based on whether the calculations were right or wrong!
        else :
            operands = calculations.split("-")
            correct = int(operands[0]) - int(operands[1]) == int(results)
        #write to files :
        if correct :
            correct_file.write(row)
        else :
            incorrect_file.write(row)