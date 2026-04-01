import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from gradebook.service import (
    add_student,
    add_course,
    enroll_student,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa
)

data = {
    "students": [],
    "courses": [],
    "enrollments": []
}

# add student
print(add_student(data, "Alice"))
print(add_student(data, "Bob"))

# add course
print(add_course(data, "CS101", "Intro to Computer Science"))
print(add_course(data, "MATH101", "Calculus"))

# enroll
print(enroll_student(data, 1, "CS101"))
print(enroll_student(data, 1, "MATH101"))
print(enroll_student(data, 2, "CS101"))

# add grades
print(add_grade(data, 1, "CS101", 90))
print(add_grade(data, 1, "CS101", 80))
print(add_grade(data, 1, "MATH101", 70))
print(add_grade(data, 2, "CS101", 85))

# list
print(list_students(data))
print(list_courses(data))
print(list_enrollments(data))

# averages
print(compute_average(data, 1, "CS101"))
print(compute_gpa(data, 1))