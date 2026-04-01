import json
import os


DEFAULT_PATH = "data/gradebook.json"


def load_data(path=DEFAULT_PATH):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }
    except json.JSONDecodeError:
        print("Error: JSON file is invalid.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }


def save_data(data, path=DEFAULT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)