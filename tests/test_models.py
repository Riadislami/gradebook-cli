
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gradebook.models import Student, Course, Enrollment

s = Student(1, "Alice")
print(str(s))

c = Course("CS101", "Intro to Computer Science")
print(str(c))

e = Enrollment(1, "CS101", [85, 90, 78])
print(str(e))