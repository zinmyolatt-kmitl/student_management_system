import tkinter as tk
from tkinter import ttk
from manager import Manager
from gui.login_page import LoginPage
from gui.home_manager import HomeManager
from gui.home_student import HomeStudent
from gui.add_page import AddStudentPage
from gui.view_page import ViewStudentsPage
from gui.search_page import SearchStudentPage
from gui.delete_page import DeleteStudentPage
from gui.edit_page import EditStudentPage
from gui.course_page import CoursePage
from gui.theme import setup_style


class StudentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Management System")

        width, height = 700, 500
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")

        setup_style(self)

        self.manager = Manager()
        self.logged_student_id = None   # set on student login

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
            LoginPage,
            HomeManager,
            HomeStudent,
            AddStudentPage,
            ViewStudentsPage,
            SearchStudentPage,
            DeleteStudentPage,
            EditStudentPage,
            CoursePage,
        ):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]

        if hasattr(frame, "load_courses"):
            frame.load_courses()

        frame.tkraise()



    def refresh_page(self, page_name: str):
        frame = self.frames[page_name]
        if hasattr(frame, "load_courses"):
            frame.load_courses() 
        frame.tkraise()

    def go_home(self):
        if self.logged_student_id:
            self.show_frame("HomeStudent")
        else:
            self.show_frame("HomeManager")

