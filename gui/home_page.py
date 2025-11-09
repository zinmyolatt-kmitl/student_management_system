import tkinter as tk
from tkinter import ttk

class HomePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")
        container.grid_rowconfigure(0, weight=1)
        container.grid_rowconfigure(1, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Title label
        title = ttk.Label(
            container,
            text="Student Management System",
            style="Title.TLabel",
            foreground="#000000",
            anchor="center"
        )
        title.grid(row=0, column=0, pady=(40, 10), sticky="n")

        # Button frame centered
        btn_frame = ttk.Frame(container)
        btn_frame.grid(row=1, column=0, sticky="nsew")
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_rowconfigure("all", weight=1)

        buttons = [
            ("Add Student", "AddStudentPage"),
            ("View Students", "ViewStudentsPage"),
            ("Search Student", "SearchStudentPage"),
            ("Delete Student", "DeleteStudentPage"),
            ("Edit Student", "EditStudentPage"),
            ("Manage Courses", "CoursePage"),
        ]


        for i, (text, page) in enumerate(buttons):
            btn = ttk.Button(
                btn_frame,
                text=text,
                command=lambda p=page: controller.show_frame(p)
            )
            btn.grid(row=i, column=0, pady=6, padx=100, ipadx=10, ipady=5, sticky="ew")

        # Add responsive padding (so buttons stay centered)
        container.grid_rowconfigure(2, weight=1)
