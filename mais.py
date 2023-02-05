from random import *
class Course:
    def __init__(self):
        self.course_id = int(input("enter cours id"))
        self.course_name =["css","java","c","c#","c++"]
        self.course_class = input("enter course class (A,B,C)")
        #self.course_name.append(self.course_class)
class Student():
    def __init__(self):
        self.student_name = input("enter student name")
        self.student_id = random.randint(10000, 99999)
        self.student_class = input("enter student class(A,B,C)")
        self.student_course = [self.student_name,self.student_class]

    def add(self, Course, course_name):
        if self.student_class == Course.course_class:
            self.student_course.append(course_name)

    def show(self):
        print("student name :", self.student_name)
        print("student class:", self.student_class)
        print("  Courses students are enrolled in", self.student_course)

#
# course = Course()
# student = Student()

print("1-Add New student\n2-Remove student\n3-Edit student\n4-Display all student\n"
      "5-creat a new course\n6-Add course to student\n0-exit")
choice = int(input("select choice please"))
course = Course()
student = Student()
if choice == 1:
    student.student_name
    student.student_class
    if student.student_class != "A" or student.student_class!= "B" or student.student_class != "C"\
            or student.student_class != "a" or student.student_class!= "b" or student.student_class!= "c":
        input("enter the class again")
    else:
        print("student saved successfully")


if choice == 2:
    student.student_id
    if student.student_id in student.student_id:
        student.student_course.remove()
        print("delete done successful")
    else:
        print("user not exist")
if choice == 3:
    student.student_id
    if student.student_id in student.student_id:
        student.student_name
        student.student_class
    else:
        print("user not exist")

if choice == 4:
    student.show()
    print(student)

if choice == 5:
    l= input("enter new course")
    course.course_name.append(l)
    course.course_class

if choice == 6:
    student.student_id
    if student.student_id in student.student_id:
        course.course_name
        if course.course_name in course.course_name:
            student.student_course.append(course.course_name)
        else:
            print("course not exist")
if choice == 0:
    exit()
