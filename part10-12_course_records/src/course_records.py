class Course:
    def __init__(self, name : str):
        self.__name = name
        self.__grade = 0
        self.__credits = 0
    
    def name(self):
        return self.__name
    
    def credits(self):
        return self.__credits
    
    def grade(self):
        return self.__grade
    
    def set_credit(self, credit: int):
        self.__credits = credit

    def set_grade(self, grade: int):
        self.__grade = grade

    def __str__(self):
        return f"{self.__name} ({self.credits()} cr) grade {self.grade()}"

class CourseSetting: 
    def __init__(self):
        self.__course_data = {}
    
    def add_course(self, name:str, credit: int, grade: int):
        if not name in self.__course_data:
            self.__course_data[name] = Course(name)
            self.__course_data[name].set_credit(credit)
            self.__course_data[name].set_grade(grade)

        if self.__course_data[name].grade() < grade:
            self.__course_data[name].set_grade(grade)
    
    def get_entry(self, name: str):
        if not name in self.__course_data:
            return None
        return self.__course_data[name]

    def all_entries(self):
        return self.__course_data
    
    def stat(self):
        sum_gr = 0
        sum_cr = 0
        grades = []
        for value in self.__course_data.values():
            sum_cr += int(value.credits())
            sum_gr += int(value.grade())
            grades.append(value.grade())
        print(f"{len(self.__course_data)} completed courses, a total of {sum_cr} credits")
        print(f"mean {round((sum_gr / len(self.__course_data)),1)}")
        print("grade distribution")  
        i = 5
        while i > 0:
            output = f"{i}: "
            for grade in grades :
                if grade == str(i):
                    output += "x"
            print(output)
            i -= 1 

class CourseApplication:
    def __init__(self):
        self.__course = CourseSetting()
    
    def help(self):
        print("commands:")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = input("grade: ")
        credit = input("credits: ")
        self.__course.add_course(name,credit,grade)

    def get_course(self):
        name = input("course: ")
        data = self.__course.get_entry(name)
        if data == None:
            print("no entry for this course")
            return
        else:
            print(data)

    def get_stat(self):
        return self.__course.stat()
    

    def execute(self):
        self.help()
        while True :
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.get_stat()
            else:
                self.help()

application = CourseApplication()
application.execute()

