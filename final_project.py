# from random import *
# class Course:
#     def __init__(self):
#         self.course_id = int(input("enter cours id"))
#         self.course_name =input("enter the name")
#         self.course_class = input("enter course class (A,B,C)")
#
#
# class Student():
#     def __init__(self):
#         self.student_name = input("enter student name")
#         self.student_id = random.randint(10000, 99999)
#         self.student_class = input("enter student class(A,B,C)")
#         self.student_course = []
#
#     def add(self, Course, course_name):
#         if self.student_class == Course.course_class:
#             self.student_course.append(course_name)
#
#     def show(self):
#         print("student name :", self.student_name)
#         print("student class:", self.student_class)
#         print("  Courses students are enrolled in", self.student_course)
#
# #
# course = Course()
# student = Student()
# print("1-Add New student\n2-Remove student\n3-Edit student\n4-Display all student\n"
#       "5-creat a new course\n6-Add course to student\n0-exit")
# choice = int(input("select choice please"))
# # course = Course()
# # student = Student()
# if choice == 1:
#     input("enter student name")
#     f=input("enter student class(A,B,C)")
#     if f != "A" or f!= "B" or f != "C"\
#             or f != "a" or f!= "b" or f!= "c":
#         input("enter the class again")
#     else:
#         print("student saved successfully")
#
#
# if choice == 2:
#     m=int(input("enter student id "))
#     if m in student.student_id:
#         print("delete done successful")
#     else:
#         print("user not exist")
# if choice == 3:
#     m = int = input("enter student id")
#     if m in student.student_id:
#         input("enter new name")
#         input("enter class (A,B,C)")
#     else:
#         print("user not exist")
#
# if choice == 4:
#     student.show()
#     print(student)
#
# if choice == 5:
#     input("enter class name")
#     input("choice course(A,B,C):")
#
# if choice == 6:
#     x = int(input("enter student number"))
#     if x in student.student_id:
#         l = input("enter name of course")
#         if l in course.course_name:
#             student.student_course.append(l)
#         else:
#             print("course not exist")
# if choice == 0:
#     exit()
