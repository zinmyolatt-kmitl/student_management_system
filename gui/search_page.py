import tkinter as tk
from tkinter import ttk, messagebox

class SearchStudentPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Search Student", style="Title.TLabel").pack(pady=20)

        form = ttk.Frame(self, padding=10)
        form.pack()

        ttk.Label(form, text="Enter Name or ID:").grid(row=0, column=0, pady=5)
        self.query_entry = ttk.Entry(form, width=30)
        self.query_entry.grid(row=0, column=1, pady=5)

        ttk.Button(self, text="Search", command=self.search_student).pack(pady=10)
        ttk.Button(self, text="Back", command=controller.go_home).pack()

        self.result_label = tk.Label(
            self,
            text="",
            font=("Helvetica", 11, "bold"),
            bg="#E8F0FE"
        )
        self.result_label.pack(pady=10)

    def search_student(self):
        query = self.query_entry.get().strip()
        if not query:
            messagebox.showerror("Error", "Please enter a name or ID.")
            return

        student = self.controller.manager.search_student(query)
        if student:
            self.result_label.config(
                text=f"Found: ID {student['id']} | {student['name']} - Grade {student['grade']}",
                fg="green"
            )
        else:
            self.result_label.config(
                text="Student not found.",
                fg="red"
            )
