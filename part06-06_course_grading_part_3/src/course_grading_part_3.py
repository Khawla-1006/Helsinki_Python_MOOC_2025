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

print(f"{"name":30}{"exec_nbr":10}{"exec_pts.":10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}")
for key1, student in students.items() :
    for key2, exercise in exercises.items() :
        for key3, grade in grades.items():
            if key1 == key2 == key3: 
                ex_sum = sum(exercise)
                ex_pts = int(ex_sum * 10 / 40)
                grade_sum = sum(grade)
                awarded_pts = int(ex_pts) + grade_sum
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
                print(f"{student:30}{ex_sum:<10}{ex_pts:<10}{grade_sum:<10}{awarded_pts:<10}{final_grade:<10}")
