# Gradebook CLI

A simple command-line application built in Python to manage students, courses, and grades.

---

## Features

- Add students
- Add courses
- Enroll students in courses
- Add grades
- List students, courses, and enrollments
- Compute average grade per course
- Compute GPA per student
- Data persistence using JSON
- Logging of actions and errors

---

## Project Structure

gradebook_cli/

├── gradebook/  
│   ├── _init_.py  
│   ├── models.py  
│   ├── service.py  
│   └── storage.py  

├── data/  
│   └── gradebook.json  

├── logs/  
│   └── app.log  

├── tests/  
│   ├── test_models.py  
│   ├── test_service.py  
│   └── test_storage.py  

├── main.py  
├── README.md  
└── .gitignore  

---

## Setup

1. Clone the repository:
    git clone https://github.com/Riadislami/gradebook-cli.git



## Usage

Add a student:
python main.py add-student --name "Riad"

Add a course:
python main.py add-course --code CS101 --title "Intro to Computer Science"

Enroll a student:
python main.py enroll --student-id 1 --course CS101

Add a grade:
python main.py add-grade --student-id 1 --course CS101 --grade 95

List data:
python main.py list students
python main.py list courses
python main.py list enrollments

Compute average:
python main.py avg --student-id 1 --course CS101

Compute GPA:
python main.py gpa --student-id 1

## Testing

python tests/test_models.py  
python tests/test_service.py  
python tests/test_storage.py


## Logging

Logs are saved in:
logs/app.log


## Notes

- Grades must be between 0 and 100
- Course codes must be unique
- Students must exist before enrollment
- Data is stored in JSON format


## Author

This project was created as a Python mini-project using basic OOP and CLI concepts.