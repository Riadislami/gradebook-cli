import argparse
import logging

from gradebook.storage import load_data, save_data
from gradebook.service import (
    add_student,
    add_course,
    enroll_student as enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa
)

# ---------------- LOGGING ----------------
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")

    subparsers = parser.add_subparsers(dest="command")

    # ---------------- ADD STUDENT ----------------
    parser_add_student = subparsers.add_parser("add-student")
    parser_add_student.add_argument("--name", required=True)

    # ---------------- ADD COURSE ----------------
    parser_add_course = subparsers.add_parser("add-course")
    parser_add_course.add_argument("--code", required=True)
    parser_add_course.add_argument("--title", required=True)

    # ---------------- ENROLL ----------------
    parser_enroll = subparsers.add_parser("enroll")
    parser_enroll.add_argument("--student-id", type=int, required=True)
    parser_enroll.add_argument("--course", required=True)

    # ---------------- ADD GRADE ----------------
    parser_add_grade = subparsers.add_parser("add-grade")
    parser_add_grade.add_argument("--student-id", type=int, required=True)
    parser_add_grade.add_argument("--course", required=True)
    parser_add_grade.add_argument("--grade", type=float, required=True)

    # ---------------- LIST ----------------
    parser_list = subparsers.add_parser("list")
    parser_list.add_argument("entity", choices=["students", "courses", "enrollments"])
    parser_list.add_argument("--sort", default=None)

    # ---------------- AVG ----------------
    parser_avg = subparsers.add_parser("avg")
    parser_avg.add_argument("--student-id", type=int, required=True)
    parser_avg.add_argument("--course", required=True)

    # ---------------- GPA ----------------
    parser_gpa = subparsers.add_parser("gpa")
    parser_gpa.add_argument("--student-id", type=int, required=True)

    args = parser.parse_args()

    data = load_data()

    try:
        # -------- ADD STUDENT --------
        if args.command == "add-student":
            student = add_student(data, args.name)
            save_data(data)
            logging.info(f"Added student: {student}")
            print(student)

        # -------- ADD COURSE --------
        elif args.command == "add-course":
            course = add_course(data, args.code, args.title)
            save_data(data)
            logging.info(f"Added course: {course}")
            print(course)

        # -------- ENROLL --------
        elif args.command == "enroll":
            enrollment = enroll(data, args.student_id, args.course)
            save_data(data)
            logging.info(f"Enrollment created: {enrollment}")
            print(enrollment)

        # -------- ADD GRADE --------
        elif args.command == "add-grade":
            enrollment = add_grade(data, args.student_id, args.course, args.grade)
            save_data(data)
            logging.info(f"Added grade: {args.grade} to {enrollment}")
            print(enrollment)

        # -------- LIST --------
        elif args.command == "list":
            if args.entity == "students":
                result = list_students(data)
            elif args.entity == "courses":
                result = list_courses(data)
            else:
                result = list_enrollments(data)

            logging.info(f"Listed {args.entity}")
            for item in result:
                print(item)

        # -------- AVG --------
        elif args.command == "avg":
            avg = compute_average(data, args.student_id, args.course)
            logging.info(f"Average computed: {avg}")
            print(f"Average: {avg:.2f}")

        # -------- GPA --------
        elif args.command == "gpa":
            gpa = compute_gpa(data, args.student_id)
            logging.info(f"GPA computed: {gpa}")
            print(f"GPA: {gpa:.2f}")

        else:
            parser.print_help()

    except ValueError as e:
        logging.error(f"ValueError: {e}")
        print(f"Error: {e}")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()