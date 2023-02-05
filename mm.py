import random


class Course:
    def __init__(self, course_id, course_name, course_class):
        self.course_id = course_id
        self.course_name = course_name
        self.course_class = course_class


class Student:
    def __init__(self, student_name, student_class):
        self.student_name = student_name
        self.student_id = random.randint(10000, 99999)
        self.student_class = student_class
        self.student_courses = []

    def add_course(self, course):
        if self.student_class == course.course_class:
            self.student_courses.append(course)
        else:
            print("Course class does not match student class")

    def display_student_details(self):
        print("Name:", self.student_name)
        print("Class:", self.student_class)
        print("Courses:")
        for course in self.student_courses:
            print(course.course_name)


def add_new_student():
    name = input("Enter student name: ")
    student_class = input("Enter class (A, B, C): ")
    while student_class not in ["A", "B", "C"]:
        student_class = input("Enter valid class (A, B, C): ")
    student = Student(name, student_class)
    print("Student saved successfully")


def remove_student(students):
    student_id = int(input("Enter student id: "))
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            print("Delete successful")
            return
    print("Student not found")


def edit_student(students):
    student_id = int(input("Enter student id: "))
    for student in students:
        if student.student_id == student_id:
            student.student_name = input("Enter new student name: ")
            student.student_class = input("Enter new class (A, B, C): ")
            while student.student_class not in ["A", "B", "C"]:
                student.student_class = input("Enter valid class (A, B, C): ")
            return
    print("Student not found")


def display_all_students(students):
    for student in students:
        student.display_student_details()


def create_new_course():
    course_id = input("Enter course id: ")
    course_name = input("Enter course name: ")
    course_class = input("Enter course class (A, B, C): ")
    while course_class not in ["A", "B", "C"]:
        course_class = input("Enter valid course class (A, B, C): ")
    course = Course(course_id, course_name, course_class)


def add_course_to_student(students, courses):
    student_id = int(input("Enter student id: "))
    for student in students:
