from tkinter import ttk


class HomeManager(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Manager Dashboard", style="Title.TLabel").pack(pady=20)

        buttons = [
            ("Add Student", "AddStudentPage"),
            ("View Students", "ViewStudentsPage"),
            ("Search Student", "SearchStudentPage"),
            ("Edit Student", "EditStudentPage"),
            ("Delete Student", "DeleteStudentPage"),
            ("Manage Courses", "CoursePage"),
            ("Logout", "LoginPage"),
        ]

        for text, page in buttons:
            ttk.Button(self, text=text, command=lambda p=page: controller.show_frame(p)).pack(
                pady=6, ipadx=20, ipady=4
            )
