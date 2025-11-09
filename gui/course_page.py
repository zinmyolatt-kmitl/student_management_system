import tkinter as tk
from tkinter import ttk, messagebox

class CoursePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Course Management", style="Title.TLabel").pack(pady=20)

        self.add_frame = ttk.Labelframe(self, text="Add Course", padding=10)
        self.add_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.add_frame, text="Course Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.course_name = ttk.Entry(self.add_frame, width=30)
        self.course_name.grid(row=0, column=1, pady=5)

        ttk.Label(self.add_frame, text="Instructor:").grid(row=1, column=0, sticky="e", pady=5)
        self.instructor = ttk.Entry(self.add_frame, width=30)
        self.instructor.grid(row=1, column=1, pady=5)

        ttk.Button(self.add_frame, text="Add Course", command=self.add_course).grid(
            row=2, column=0, columnspan=2, pady=10
        )

        self.del_frame = ttk.Labelframe(self, text="Delete Course", padding=10)
        self.del_frame.pack(padx=10, pady=10, fill="x")

        ttk.Label(self.del_frame, text="Course Name:").grid(row=0, column=0, sticky="e", pady=5)
        self.delete_entry = ttk.Entry(self.del_frame, width=30)
        self.delete_entry.grid(row=0, column=1, pady=5)

        ttk.Button(self.del_frame, text="Delete Course", command=self.delete_course).grid(
            row=1, column=0, columnspan=2, pady=10
        )

        ttk.Label(self, text="All Courses", font=("Helvetica", 13, "bold")).pack(pady=(15, 5))
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

        btn_frame = ttk.Frame(self)
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="Load Courses", command=self.load_courses).grid(row=0, column=0, padx=5)
        ttk.Button(btn_frame, text="Back", command=self.go_back).grid(row=0, column=1, padx=5)

    def add_course(self):
        name = self.course_name.get().strip()
        instructor = self.instructor.get().strip()
        if not name or not instructor:
            messagebox.showerror("Error", "Please fill all fields.")
            return
        added = self.controller.manager.add_course(name, instructor)
        if added:
            messagebox.showinfo("Success", f"Course '{name}' added successfully.")
            self.course_name.delete(0, tk.END)
            self.instructor.delete(0, tk.END)
            self.load_courses()
        else:
            messagebox.showerror("Error", f"Course '{name}' already exists.")

    def delete_course(self):
        name = self.delete_entry.get().strip()
        if not name:
            messagebox.showerror("Error", "Please enter a course name.")
            return
        removed = self.controller.manager.delete_course(name)
        if removed:
            messagebox.showinfo("Success", f"Course '{name}' deleted.")
            self.delete_entry.delete(0, tk.END)
            self.load_courses()
        else:
            messagebox.showerror("Error", "Course not found.")

    def load_courses(self):
        self.text.config(state="normal")
        self.text.delete(1.0, tk.END)
        courses = self.controller.manager.get_all_courses()
        if not courses:
            self.text.insert(tk.END, "No courses available.\n")
        else:
            for i, c in enumerate(courses, start=1):
                self.text.insert(
                    tk.END, f"{i}. {c['name']} (Instructor: {c['instructor']})\n"
                )
        self.text.config(state="disabled")

        if self.controller.logged_student_id:
            self.add_frame.pack_forget()
            self.del_frame.pack_forget()
        else:
            self.add_frame.pack(padx=10, pady=10, fill="x")
            self.del_frame.pack(padx=10, pady=10, fill="x")

    def go_back(self):
        if self.controller.logged_student_id:
            self.controller.show_frame("HomeStudent")
        else:
            self.controller.show_frame("HomeManager")
