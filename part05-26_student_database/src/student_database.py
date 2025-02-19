# Write your solution here
def add_student(students : dict, student : str):
    students[student] = "no completed courses"

def print_student(students : dict , student : str) :
    if student in students :
        if students[student] != "no completed courses" :
            print(f"{student}:")
            print(f" {len(students[student])} completed courses:")
            cs = 0
            for c in students[student] :
                print(f"  {c[0]} {c[1]}", end = "\n")
                cs += c[1]
            av = cs / len(students[student])
            print(f" average grade {av}")
        else:
            print(f"{student}:")
            print(f" {students[student]}")
    else :
        print(f"{student}: no such person in the database")
        
def add_course(students : dict , student : str, course_info : tuple) :
    if course_info[1] > 0 :
        if students[student] != "no completed courses" :
            for course in students[student] :
                if course[0] == course_info[0] :
                    if course_info[1] <= course[1] :
                        return
                    else :
                        students[student].remove(course)            
            students[student].append(course_info)
        else :
            students.update({student :[course_info]})

def summary(students):
    st = 0
    max_c = 0
    m = "" 
    b = ""
    avv = []
    b_av = 0
    for key, value in students.items():
        if value != "no completed courses":
            st += 1
            if len(value) > max_c :
                max_c = len(value)
                m = key
    for key, value in students.items():
        sum_v = 0
        for val in value :
            sum_v += val[1]
        av = sum_v / len(value)
        avv.append((av,key))
    for av in avv :
        if av[0] > b_av :
            b_av = av[0]
            b = av[1]
            
    print(f"students {st}") 
    print(f"most courses completed {max_c} {m}")
    print(f"best average grade {b_av} {b}")

if __name__ == "__main__" :
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    