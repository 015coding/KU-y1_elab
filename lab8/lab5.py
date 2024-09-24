class Course:
    def __init__(self, title, code, credit):
        self.title = title
        self.course_id = code
        self.credit = credit

class Teacher:
    def __init__(self, firstname, lastname, id):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.id})"

class Major:
    def __init__(self, id, name, faculty):
        self.id = id
        self.name = name
        self.faculty = faculty

    def __str__(self):
        return f"{self.name} {self.faculty}({self.id})"


class Student:
    def __init__(self, id, firstname, lastname):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.course = []
        self.num_course = []
        self.total_credit = 0
        self.advisor = None
        self.major = None

    def add_course(self, course):
        if self.total_credit + course.credit <= 25 and course.title not in self.course:
            self.course.append(course.title)
            self.num_course.append(course.course_id)
            self.total_credit += course.credit
            return True
        return False

    def drop_course(self, course):
        if self.course[-1] == course.title:
            self.course.append("")
            self.course.remove(course.title)
            self.num_course.remove(course.course_id)
            self.total_credit -= course.credit
            return True

        elif (len(self.course) > 0 and course.title in self.course):
            self.course.remove(course.title)
            self.num_course.remove(course.course_id)
            self.total_credit -= course.credit
            return True
        return False

    def set_advisor(self, advisor):
        self.advisor = advisor

    def set_major(self, major):
        self.major = major

    def __str__(self) :


        # return (f"Student ID: {self.id}\nName: {self.firstname} {self.lastname}\nMajor: {self.major} ({Major})\nAdvisor: {Teacher}\nnourses: {' '.join(self.num_course)}")
         return (f"Student ID: {self.id}\n"
                 f"Name: {self.firstname} {self.lastname}\n"
                 f"Major: {self.major}\n"
                 f"Advisor: {self.advisor}\n"
                 f"Courses: {' '.join(str(course.course_id) for course in self.course)}")

course = ("01219111 01219113 01219245 01219221 01204212 01219213 01420113 01420114 01420111").split()
ad = Teacher("Preeda", "Lerdpongvipusana", "E901")
m = Major("E17", "Software & Knowledge Engineering", "Engineering")
s = Student(5610546231, "Chinnaporn", "Soonue")
s.set_advisor(ad)
s.set_major(m)
for i in course:
    s.add_course(Course("sth", i, 1))

print(s)
