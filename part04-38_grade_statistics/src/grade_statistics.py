# Write your solution here
def statistics(total_pts : list, ex_pts : list) :
    pt_average = round(sum(total_pts) / len(total_pts), 1)
    print(f"Points average:{pt_average : .1F}")
    grades = []
    grade = 0 
    for ex_pt , total in zip(ex_pts , total_pts):
        if ex_pt >= 10 :
            if total > 27 :
                grade = 5 
            elif total > 23 :
                grade = 4
            elif total > 20 :
                grade = 3 
            elif total > 17 :
                grade = 2 
            elif total > 14 :
                grade = 1 
            else :
                grade = 0
            grades.append(grade)
        else :
            grade = 0
            grades.append(grade)
    passed = 0
    for grade_result in grades :
        if grade_result > 0 :
            passed += 1
    pass_percentage = round(passed / len(grades) * 100 , 1)
    print(f"Pass percentage: {pass_percentage}")
    #Grade_distribution
    print("Grade distribution:")
    for i in range(5,-1,-1) :
        dis = f"{i}: "
        for gr in grades :
            if gr == i :
                dis += "*"
        print(dis)

def analyze(exam_pts_list : list, exe_list : list) :
    total_pts = []
    for pts , exe in zip(exam_pts_list,exe_list) :
        total_pts.append(pts + (exe / 10))
    statistics(total_pts, exam_pts_list)
    
def main() :
    exam_pts = []
    number_of_exe =[]
    while True :
        input_string = input("Exam points and exercises completed:")
        if input_string == "":
            break
        spliced = input_string.split()
        exam_pts.append(int(spliced[0]))
        number_of_exe.append(int(spliced[1]))
    print("Statistics:")
    analyze(exam_pts, number_of_exe)

main()