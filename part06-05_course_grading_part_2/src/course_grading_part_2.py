#The actual functionality of the program is 
#now "hidden" in the False branch of an if statement. 
#It will never be executed.
if True :
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points:")
else : 
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

students = {}
with open(student_info) as student_file :
    for line in student_file :
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1].strip() + " " + parts[2].strip()

exercises = {}

with open(exercise_data) as student_ex :
    for l in student_ex :
        p = l.split(";")
        if p[0] == "id":
            continue
        exercises[p[0]] = []
        for grade in p[1 : ]:
            exercises[p[0]].append(int(grade))

grades = {}

with open(exam_data) as exam : 
    for e in exam :
        exa = e.split(";")
        if exa[0] == "id" :
            continue
        grades[exa[0]] = []
        for g in exa[1 : ]:
            grades[exa[0]].append(int(g))


for key1, student in students.items() :
    for key2, exercise in exercises.items() :
        for key3, grade in grades.items():
            if key1 == key2 == key3: 
                ex_sum = sum(exercise) * 10 / 40 
                grade_sum = sum(grade)
                awarded_pts = float(ex_sum) + grade_sum
                if awarded_pts >= 28 : 
                    final_grade = 5 
                elif awarded_pts >= 24 :
                    final_grade = 4 
                elif awarded_pts >= 21 :
                    final_grade = 3 
                elif awarded_pts >= 18 :
                    final_grade = 2 
                elif awarded_pts >= 15 :
                    final_grade = 1 
                else :
                    final_grade = 0

                print(student,final_grade)