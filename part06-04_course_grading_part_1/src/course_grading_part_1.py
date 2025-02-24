# write your solution
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

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

for key, student in students.items() :
    for exercise , grade in exercises.items() :
        if key == exercise : 
            grade_sum = sum(grade)
            print(student,grade_sum)