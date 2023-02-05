import random
class Course :
    def __init__(self,course_id,course_name,course_class):
        self.course_id=course_id
        self.course_name=course_name
        self.course_class=course_class
class Student:
    def __init__(self,student_name,student_class):
        self.student_name=student_name
        self.student_id=random.randint(1,1000)
        self.student_class=student_class
        self.student_course=[]
    def add(self,Course):

        if self.student_class==Course.course_class:
            self.student_course.append(Course)
    def display(self):
        print("student name :",self.student_name)
        print("student class:",self.student_class)
        print("courses:")
        for Course in self.student_course:
            print(Course.course_name)
def main():
    =[]
    courses=["math","java","c"]
    while True:
        print("1-Add New student\n2-Remove student\n3-Edit student\n4-Display all student\n"
       "5-creat a new course\n6-Add course to student\n0-exit")
        choice=int(input("enter number"))
        if choice==1:
            student_name=input("enter student new name")
            student_class=input("enter class(A,B,C)")
            while student_class not in ["A","B","C","a","b","c"]:
                input("enter the class again")
                break
            new_studente=Student(student_name,student_class)
            .append(new_studente)
            print("Student saved successfully.")
        if choice==2:
            student_id=int(input("enter student id"))
            for student in student_id:
                if student.student_id == student_id:
                    .remove(student)
                    print("Delete done successfully.")
                    break
                else:
                    print("Error: Student not found.")
        if choice==3:
            student_id=int(input("enter student id"))
            for student in :
                if student.student_id==student_id:
                    student.student_name = input("Enter new student name: ")
                    student.student_class = input("Enter new student class (A, B, or C): ")
                    while student.student_class not in ["A", "B", "C"]:
                        student.student_class = input("Error")
        if choice ==4:
            for student in :
                student.display()
        if choice==5:
            class_name=input("enter class name")
            course_class=input("enter class(A,B,C)")
            courses.append(class_name,course_class)
        if choice==6:
            student_id=int(input("enter student number"))
            for student in :
                if student.student_id==student_id:
                    course_name=input("enter course name")
                    if courses in course_name:
                        student.student_course.append(courses)
                    else:
                        print("course not exist")

        if  choice==0:
            exit()
