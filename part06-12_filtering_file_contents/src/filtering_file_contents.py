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
        