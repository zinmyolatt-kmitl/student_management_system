import tkinter as tk
from tkinter import ttk, messagebox

class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Login", style="Title.TLabel").pack(pady=20)

        form = ttk.Frame(self, padding=10)
        form.pack()

        ttk.Label(form, text="Role:").grid(row=0, column=0, pady=5, sticky="e")
        self.role = ttk.Combobox(form, values=["Manager", "Student"], state="readonly", width=20)
        self.role.grid(row=0, column=1, pady=5)
        self.role.current(0)

        ttk.Label(form, text="Name or Student ID:").grid(row=1, column=0, pady=5, sticky="e")
        self.name_entry = ttk.Entry(form, width=30)
        self.name_entry.grid(row=1, column=1, pady=5)

        ttk.Button(self, text="Login", command=self.login).pack(pady=15)

    def login(self):
        role = self.role.get()
        name_or_id = self.name_entry.get().strip()

        if not name_or_id:
            messagebox.showerror("Error", "Please enter your name or student ID.")
            return

        if role == "Manager":
            self.controller.logged_student_id = None
            self.controller.show_frame("HomeManager")
            return

        student = self.controller.manager.search_student(name_or_id)
        if student:
            self.controller.logged_student_id = student["id"]
            messagebox.showinfo("Welcome", f"Welcome {student['name']}!")
            self.controller.show_frame("HomeStudent")
        else:
            messagebox.showerror("Login Failed", "No matching student found in the list.")
