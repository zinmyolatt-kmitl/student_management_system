from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def role(self):
        pass


class Student(User):
    def __init__(self, student_id, name, age, grade, courses=None):
        super().__init__(student_id, name)
        self.student_id = student_id     
        self.age = age
        self.grade = grade
        self.courses = courses or []   

    def add_course(self, course_name: str):
        if course_name not in self.courses:
            self.courses.append(course_name)

    def to_dict(self):
        return {
            "id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade,
            "courses": self.courses,
        }

    def get_info(self):
        courses = ", ".join(self.courses) if self.courses else "No courses"
        return f"Student {self.name} (ID: {self.student_id}), Grade {self.grade}, Courses: {courses}"

    def role(self):
        return "Student"


class StudentManager(User):
    def __init__(self, user_id: str = "admin001", name: str = "System Manager"):
        super().__init__(user_id, name)
        self.students: list[Student] = []

    def get_info(self) :
        return f"Manager {self.name}, Total Students: {len(self.students)}"

    def role(self):
        return "Manager"


class CourseManager(User):
    def __init__(self, user_id: str = "course_admin", name: str = "Course Manager"):
        super().__init__(user_id, name)
        self.courses: list[dict] = []  

    def add_course(self, name: str, instructor: str) :
        if any(c["name"] == name for c in self.courses):
            return False
        self.courses.append({"name": name, "instructor": instructor})
        return True

    def delete_course(self, name: str):
        for c in self.courses:
            if c["name"] == name:
                self.courses.remove(c)
                return True
        return False

    def list_courses(self):
        return self.courses

    def get_info(self):
        return f"{self.name} manages {len(self.courses)} courses."

    def role(self) :
        return "Course Manager"
