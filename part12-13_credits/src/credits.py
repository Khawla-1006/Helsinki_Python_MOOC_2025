from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    return reduce(lambda sum_credits, course : sum_credits + course.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    return reduce(lambda sum_p_c , course : sum_p_c + course.credits,list(filter(lambda course : course.grade >= 1, attempts)),0)

def average(attempts: list):
    passed_attempts = list(filter(lambda course: course.grade >= 1,attempts))
    sum_of_passed_grades = reduce(lambda sum_grade, course : sum_grade + course.grade, passed_attempts, 0)
    if len(passed_attempts) > 0 :
        return float(sum_of_passed_grades/len(passed_attempts))
    else:
        print("No passed course available !")

if __name__ =="__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
    credit_sum = sum_of_all_credits([s1, s2, s3])
    print(credit_sum)

    credit_sum = sum_of_passed_credits([s1, s2, s3])
    print(credit_sum)

    ag = average([s1, s2, s3])
    print(ag)