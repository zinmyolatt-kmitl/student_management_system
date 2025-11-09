from tkinter import ttk, messagebox

class DeleteStudentPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        ttk.Label(self, text="Delete Student", style="Title.TLabel").pack(pady=20)
        form = ttk.Frame(self, padding=10)
        form.pack()

        ttk.Label(form, text="Enter Student ID:").grid(row=0, column=0, pady=5)
        self.id_entry = ttk.Entry(form, width=30)
        self.id_entry.grid(row=0, column=1, pady=5)

        ttk.Button(self, text="Delete", command=self.delete_student).pack(pady=10)
        ttk.Button(self, text="Back", command=controller.go_home).pack()

    def delete_student(self):
        student_id = self.id_entry.get().strip()
        if not student_id:
            messagebox.showerror("Error", "Please enter a student ID.")
            return

        result = self.controller.manager.delete_student(student_id)
        if result:
            messagebox.showinfo("Success", f"Student ID {student_id} deleted.")
        else:
            messagebox.showerror("Error", "Student not found.")
        self.id_entry.delete(0, "end")
