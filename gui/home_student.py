import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.simpledialog as sd


class HomeStudent(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Student Dashboard", style="Title.TLabel").pack(pady=20)


        ttk.Button(
            self,
            text="View Available Courses",
            command=self.view_courses
        ).pack(pady=5)

        ttk.Button(
            self,
            text="Register for a Course",
            command=self.register_course
        ).pack(pady=5)

        ttk.Button(
            self,
            text="Logout",
            command=self.logout
        ).pack(pady=10)

        self.my_courses_label = ttk.Label(
            self,
            text="My Registered Courses",
            font=("Helvetica", 11, "bold"),
            foreground="blue",
            cursor="hand2"
        )
        self.my_courses_label.pack(pady=(10, 5))
        self.my_courses_label.bind("<Button-1>", lambda e: self.show_registered_courses())

        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        self.text = tk.Text(
            frame,
            wrap="word",
            font=("Consolas", 11),
            bg="#1E1E1E",
            fg="white",
            insertbackground="white",
            yscrollcommand=scrollbar.set,
            state="disabled",
        )
        self.text.pack(fill="both", expand=True)
        scrollbar.config(command=self.text.yview)

    # --- Helper for text box ---
    def _set_text(self, content):
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, content)
        self.text.config(state="disabled")

    def view_courses(self):
        courses = self.controller.manager.get_all_courses()
        if not courses:
            self._set_text("No available courses.\n")
            return

        lines = [f"- {c['name']} (Instructor: {c['instructor']})" for c in courses]
        self._set_text("Available Courses:\n\n" + "\n".join(lines))

    def register_course(self):
        sid = self.controller.logged_student_id
        if not sid:
            messagebox.showerror("Error", "No student ID is logged in.")
            return

        course_name = sd.askstring("Register Course", "Enter course name:")
        if not course_name:
            return

        success, msg = self.controller.manager.register_course(sid, course_name.strip())
        if success:
            messagebox.showinfo("Success", msg)
            self.show_registered_courses()
        else:
            messagebox.showerror("Error", msg)

    def show_registered_courses(self):
        sid = self.controller.logged_student_id
        if not sid:
            self._set_text("No student is logged in.\n")
            return

        student = next((s for s in self.controller.manager.students if s.student_id == sid), None)
        if not student:
            self._set_text("Student record not found.\n")
            return

        if not student.courses:
            self._set_text("You haven't registered for any courses yet.\n")
            return

        lines = [f"{i}. {c}" for i, c in enumerate(student.courses, start=1)]
        self._set_text("My Registered Courses:\n\n" + "\n".join(lines))

    def logout(self):
        self.controller.logged_student_id = None
        self.controller.show_frame("LoginPage")
