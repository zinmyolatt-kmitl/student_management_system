import tkinter as tk
from tkinter import ttk, messagebox

class AddStudentPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Add Student", style="Title.TLabel", foreground="#000000").pack(pady=20)

        form = ttk.Frame(self, padding=10)
        form.pack()

        ttk.Label(form, text="Student ID:", foreground="#000000").grid(row=0, column=0, sticky="e", pady=5)
        self.id_entry = ttk.Entry(form, width=30)
        self.id_entry.grid(row=0, column=1, pady=5)

        ttk.Label(form, text="Name:", foreground="#000000").grid(row=1, column=0, sticky="e", pady=5)
        self.name_entry = ttk.Entry(form, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        ttk.Label(form, text="Age:", foreground="#000000").grid(row=2, column=0, sticky="e", pady=5)
        self.age_entry = ttk.Entry(form, width=30)
        self.age_entry.grid(row=2, column=1, pady=5)

        ttk.Label(form, text="Grade:", foreground="#000000").grid(row=3, column=0, sticky="e", pady=5)
        self.grade_entry = ttk.Entry(form, width=30)
        self.grade_entry.grid(row=3, column=1, pady=5)

        ttk.Button(self, text="Add Student", command=self.add_student).pack(pady=15)
        ttk.Button(self, text="Back", command=controller.go_home).pack()

    def add_student(self):
        student_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        grade = self.grade_entry.get().strip().upper()

        if not student_id or not name or not age or not grade:
            messagebox.showerror("Error", "Please fill all fields.")
            return

        try:
            age = int(age)
            if age <= 0:
                messagebox.showerror("Error", "Age must be a positive number.")
                return
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid number.")
            return

        valid_grades = ["A+", "A", "B", "C", "D", "F"]
        if grade not in valid_grades:
            messagebox.showerror("Error", f"Invalid grade '{grade}'. Valid grades: {', '.join(valid_grades)}")
            return

        self.controller.manager.add_student(student_id, name, age, grade)
        messagebox.showinfo("Success", f"Student '{name}' added successfully.")

        for entry in [self.id_entry, self.name_entry, self.age_entry, self.grade_entry]:
            entry.delete(0, tk.END)
