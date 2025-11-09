import tkinter as tk
from tkinter import ttk, messagebox

class EditStudentPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Edit Student Information", style="Title.TLabel").pack(pady=20)

        search_frame = ttk.Frame(self, padding=10)
        search_frame.pack()

        ttk.Label(search_frame, text="Enter ID or Name:").grid(row=0, column=0, pady=5)
        self.search_entry = ttk.Entry(search_frame, width=30)
        self.search_entry.grid(row=0, column=1, pady=5)
        ttk.Button(search_frame, text="Find", command=self.find_student).grid(row=0, column=2, padx=10)

        form = ttk.Frame(self, padding=10)
        form.pack()

        ttk.Label(form, text="Student ID:").grid(row=0, column=0, sticky="e", pady=5)
        self.id_entry = ttk.Entry(form, width=30)
        self.id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(form, text="Name:").grid(row=1, column=0, sticky="e", pady=5)
        self.name_entry = ttk.Entry(form, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        ttk.Label(form, text="Age:").grid(row=2, column=0, sticky="e", pady=5)
        self.age_entry = ttk.Entry(form, width=30)
        self.age_entry.grid(row=2, column=1, pady=5)

        ttk.Label(form, text="Grade:").grid(row=3, column=0, sticky="e", pady=5)
        self.grade_entry = ttk.Entry(form, width=30)
        self.grade_entry.grid(row=3, column=1, pady=5)

        ttk.Button(self, text="Save Changes", command=self.save_changes).pack(pady=15)
        ttk.Button(self, text="Back", command=controller.go_home).pack()

    def find_student(self):
        query = self.search_entry.get().strip()
        student = self.controller.manager.search_student(query)

        if not student:
            messagebox.showerror("Not Found", "Student not found.")
            return

        self.id_entry.delete(0, tk.END)
        self.id_entry.insert(0, student["id"])
        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, student["name"])
        self.age_entry.delete(0, tk.END)
        self.age_entry.insert(0, student["age"])
        self.grade_entry.delete(0, tk.END)
        self.grade_entry.insert(0, student["grade"])

    def save_changes(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        grade = self.grade_entry.get().strip().upper()

        if not all([student_id, name, age, grade]):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            age = int(age)
            if age <= 0:
                messagebox.showerror("Error", "Age must be a positive number.")
                return
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid number.")
            return

        valid_grades = ["A+", "A", "B+", "B", "C+", "C", "D", "F"]
        if grade not in valid_grades:
            messagebox.showerror("Error", f"Invalid grade '{grade}'. Valid grades: {', '.join(valid_grades)}")
            return

        updated = self.controller.manager.update_student(student_id, name, age, grade)
        if updated:
            messagebox.showinfo("Success", "Student information updated successfully.")
        else:
            messagebox.showerror("Error", "Student not found.")
