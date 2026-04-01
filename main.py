import argparse

from gradebook.storage import load_data, save_data
from gradebook.service import (
    add_student,
    add_course,
    enroll_student,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa,
)


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    # add-student
    parser_add_student = subparsers.add_parser("add-student", help="Add a new student")
    parser_add_student.add_argument("--name", required=True, help="Student name")

    # add-course
    parser_add_course = subparsers.add_parser("add-course", help="Add a new course")
    parser_add_course.add_argument("--code", required=True, help="Course code")
    parser_add_course.add_argument("--title", required=True, help="Course title")

    # enroll
    parser_enroll = subparsers.add_parser("enroll", help="Enroll student in course")
    parser_enroll.add_argument("--student-id", type=int, required=True, help="Student ID")
    parser_enroll.add_argument("--course", required=True, help="Course code")

    # add-grade
    parser_add_grade = subparsers.add_parser("add-grade", help="Add grade to enrollment")
    parser_add_grade.add_argument("--student-id", type=int, required=True, help="Student ID")
    parser_add_grade.add_argument("--course", required=True, help="Course code")
    parser_add_grade.add_argument("--grade", type=float, required=True, help="Grade value")

    # list
    parser_list = subparsers.add_parser("list", help="List data")
    parser_list.add_argument("entity", choices=["students", "courses", "enrollments"])
    parser_list.add_argument("--sort", default=None, help="Sort field")

    # avg
    parser_avg = subparsers.add_parser("avg", help="Compute course average for a student")
    parser_avg.add_argument("--student-id", type=int, required=True, help="Student ID")
    parser_avg.add_argument("--course", required=True, help="Course code")

    # gpa
    parser_gpa = subparsers.add_parser("gpa", help="Compute GPA for a student")
    parser_gpa.add_argument("--student-id", type=int, required=True, help="Student ID")

    args = parser.parse_args()
    data = load_data()

    try:
        if args.command == "add-student":
            student = add_student(data, args.name)
            save_data(data)
            print(f"Student added successfully: {student}")

        elif args.command == "add-course":
            course = add_course(data, args.code, args.title)
            save_data(data)
            print(f"Course added successfully: {course}")

        elif args.command == "enroll":
            enrollment = enroll_student(data, args.student_id, args.course)
            save_data(data)
            print(f"Enrollment successful: {enrollment}")

        elif args.command == "add-grade":
            enrollment = add_grade(data, args.student_id, args.course, args.grade)
            save_data(data)
            print(f"Grade added successfully: {enrollment}")

        elif args.command == "list":
            if args.entity == "students":
                students = list_students(data)
                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(student)

            elif args.entity == "courses":
                courses = list_courses(data)
                if not courses:
                    print("No courses found.")
                else:
                    for course in courses:
                        print(course)

            elif args.entity == "enrollments":
                enrollments = list_enrollments(data)
                if not enrollments:
                    print("No enrollments found.")
                else:
                    for enrollment in enrollments:
                        print(enrollment)

        elif args.command == "avg":
            average = compute_average(data, args.student_id, args.course)
            print(f"Average: {average:.2f}")

        elif args.command == "gpa":
            gpa = compute_gpa(data, args.student_id)
            print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()

    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()