import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from gradebook.storage import load_data, save_data

# load (kur nuk ka file)
data = {
    "students": [],
    "courses": [],
    "enrollments": []
}
print("Initial:", data)

# shto diçka
data["students"].append({"id": 1, "name": "Alice"})
data["courses"].append({"code": "CS101", "title": "Intro to Computer Science"})
data["enrollments"].append({"student_id": 1, "course_code": "CS101", "grades": [85, 90, 78]})

# save
save_data(data)

# load prap
data2 = load_data()
print("After save:", data2)