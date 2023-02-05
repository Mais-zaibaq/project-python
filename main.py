import random


class Course:
    def __init__(self, course_id, course_name, course_class):
        self.course_id = course_id
        self.course_name = course_name
        self.course_class = course_class


class Student:
    def __init__(self, student_name, student_class):
        self.student_id = random.randint(10000, 99999)
        self.student_name = student_name
        self.student_class = student_class
        self.student_courses = []

    def add_course(self, course):
        if self.student_class == course.course_class:
            self.student_courses.append(course)
        else:
            print("This course is not available for this student's class.")

    def display_student_details(self):
        print("Name:", self.student_name)
        print("Class:", self.student_class)
        print("Enrolled courses:")
        for course in self.student_courses:
            print(course.course_name)


def main():
    students = []
    courses = []

    while True:
        print("1. Add new student")
        print("2. Remove student")
        print("3. Edit student")
        print("4. Display all students")
        print("5. Create new course")
        print("6. Add course to student")
        print("0. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            student_name = input("Enter student name: ")
            student_class = input("Enter student class (A, B, or C): ")
            while student_class not in ["A", "B", "C"]:
                student_class = input("Enter student class (A, B, or C): ")
            students.append(Student(student_name, student_class))
            print("Student saved successfully.")
        elif choice == 2:
            student_id = int(input("Enter student id: "))
            student_found = False
            for student in students:
                if student.student_id == student_id:
                    students.remove(student)
                    student_found = True
                    print("Delete done successfully.")
                    break
            if not student_found:
                print("User not found.")
        elif choice == 3:
            student_id = int(input("Enter student id: "))
            student_found = False
            for student in students:
                if student.student_id == student_id:
                    student_name = input("Enter new student name: ")
                    student_class = input("Enter new student class (A, B, or C): ")
                    while student_class not in ["A", "B", "C"]:
                        student_class = input("Enter student class (A, B, or C): ")
                    student.student_name = student_name
                    student.student_class = student_class
                    student_found = True
                    print("Edit done successfully.")
                    break
            if not student_found:
                print("User not found")
