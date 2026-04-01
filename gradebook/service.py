def add_student(data, name):
    """Add a new student."""
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name cannot be empty.")

    next_id = 1
    if data["students"]:
        next_id = max(student["id"] for student in data["students"]) + 1

    student = {
        "id": next_id,
        "name": name.strip()
    }

    data["students"].append(student)
    return student


def add_course(data, code, title):
    """Add a new course."""
    if not isinstance(code, str) or not code.strip():
        raise ValueError("Course code cannot be empty.")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Course title cannot be empty.")

    for course in data["courses"]:
        if course["code"] == code:
            raise ValueError("Course code already exists.")

    course = {
        "code": code.strip(),
        "title": title.strip()
    }

    data["courses"].append(course)
    return course


def enroll_student(data, student_id, course_code):
    """Enroll a student in a course."""
    student_exists = any(student["id"] == student_id for student in data["students"])
    if not student_exists:
        raise ValueError("Student not found.")

    course_exists = any(course["code"] == course_code for course in data["courses"])
    if not course_exists:
        raise ValueError("Course not found.")

    already_enrolled = any(
        enrollment["student_id"] == student_id and enrollment["course_code"] == course_code
        for enrollment in data["enrollments"]
    )

    if already_enrolled:
        raise ValueError("Student is already enrolled in this course.")

    enrollment = {
        "student_id": student_id,
        "course_code": course_code,
        "grades": []
    }

    data["enrollments"].append(enrollment)
    return enrollment


def add_grade(data, student_id, course_code, grade):
    """Add a grade for a student's enrollment."""
    if not isinstance(grade, (int, float)):
        raise ValueError("Grade must be a number.")
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            enrollment["grades"].append(grade)
            return enrollment

    raise ValueError("Enrollment not found.")


def list_students(data):
    """Return students sorted by name."""
    return sorted(data["students"], key=lambda student: student["name"])


def list_courses(data):
    """Return courses sorted by code."""
    return sorted(data["courses"], key=lambda course: course["code"])


def list_enrollments(data):
    """Return enrollments sorted by student_id and course_code."""
    return sorted(
        data["enrollments"],
        key=lambda enrollment: (enrollment["student_id"], enrollment["course_code"])
    )


def compute_average(data, student_id, course_code):
    """Compute average grade for one enrollment."""
    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            if not enrollment["grades"]:
                raise ValueError("No grades available for this enrollment.")
            return sum(enrollment["grades"]) / len(enrollment["grades"])

    raise ValueError("Enrollment not found.")


def compute_gpa(data, student_id):
    """Compute GPA as average of all enrollment averages for a student."""
    averages = []

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["grades"]:
            avg = sum(enrollment["grades"]) / len(enrollment["grades"])
            averages.append(avg)

    if not averages:
        raise ValueError("No grades available for this student.")

    return sum(averages) / len(averages)