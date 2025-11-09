import json
from model import Student, StudentManager, CourseManager


class Manager(StudentManager):
    def __init__(self):
        super().__init__()
        self.course_manager = CourseManager()
        self.load_from_file()

    def add_student(self, student_id, name, age, grade):
        for s in self.students:
            if s.student_id == student_id:
                s.name = name
                s.age = age
                s.grade = grade
                self.save_to_file()
                return "updated"

        new_student = Student(student_id, name, age, grade)
        self.students.append(new_student)
        self.save_to_file()
        return "added"

    def update_student(self, student_id, name=None, age=None, grade=None):
        return self.edit_student(student_id, name, age, grade)



    def get_all_students(self):
        return [
            {
                "id": s.student_id,
                "name": s.name,
                "age": s.age,
                "grade": s.grade,
                "courses": s.courses,
            }
            for s in self.students
        ]


    def search_student(self, query):
        query = query.lower()
        for s in self.students:
            if s.student_id.lower() == query or s.name.lower() == query:
                return {
                    "id": s.student_id,
                    "name": s.name,
                    "age": s.age,
                    "grade": s.grade,
                    "courses": s.courses,
                }
        return None

    def delete_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                self.students.remove(s)
                self.save_to_file()
                return True
        return False

    def edit_student(self, student_id, name=None, age=None, grade=None):
        for s in self.students:
            if s.student_id == student_id:
                if name:
                    s.name = name
                if age:
                    s.age = age
                if grade:
                    s.grade = grade
                self.save_to_file()
                return True
        return False

    def add_course(self, name, instructor):
        return self.course_manager.add_course(name, instructor)

    def delete_course(self, name):
        return self.course_manager.delete_course(name)

    def get_all_courses(self):
        return self.course_manager.list_courses()

    def register_course(self, student_id, course_name):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if not student:
            return False, "Student not found."

        course = next(
            (c for c in self.course_manager.courses if c["name"].lower() == course_name.lower()),
            None,
        )
        if not course:
            return False, f"Course '{course_name}' not found."

        if course["name"] in student.courses:
            return False, f"Already registered for '{course_name}'."

        student.add_course(course["name"])
        self.save_to_file()
        return True, f"Successfully registered for '{course['name']}'."

 
    def save_to_file(self):
        data = {
            "students": [s.to_dict() for s in self.students],
            "courses": self.course_manager.courses,
        }
        with open("students.json", "w") as f:
            json.dump(data, f, indent=4)

    def load_from_file(self):
        try:
            with open("students.json", "r") as f:
                data = json.load(f)

            if isinstance(data, list):
                self.students = [
                    Student(s["id"], s["name"], s["age"], s["grade"], s.get("courses", []))
                    for s in data
                ]
                self.course_manager.courses = []
                return

            self.students = [
                Student(s["id"], s["name"], s["age"], s["grade"], s.get("courses", []))
                for s in data.get("students", [])
            ]
            self.course_manager.courses = data.get("courses", [])

        except FileNotFoundError:
            self.students = []
            self.course_manager.courses = []
