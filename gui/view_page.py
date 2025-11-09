import tkinter as tk
from tkinter import ttk

class ViewStudentsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        main_container = ttk.Frame(self)
        main_container.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


        main_container.grid_rowconfigure(2, weight=1)
        main_container.grid_columnconfigure(0, weight=1)

        title = ttk.Label(main_container, text="All Students", style="Title.TLabel")
        title.grid(row=0, column=0, pady=(0, 20))

        controls_frame = ttk.Frame(main_container)
        controls_frame.grid(row=1, column=0, pady=(0, 10))

        ttk.Button(controls_frame, text="Sort by Name", command=lambda: self.load_students(sort_key="name")).grid(row=0, column=0, padx=5)
        ttk.Button(controls_frame, text="Sort by Age", command=lambda: self.load_students(sort_key="age")).grid(row=0, column=1, padx=5)
        ttk.Button(controls_frame, text="Sort by Grade", command=lambda: self.load_students(sort_key="grade")).grid(row=0, column=2, padx=5)

        ttk.Label(controls_frame, text="Filter Grade:").grid(row=0, column=3, padx=(20, 5))
        self.filter_var = tk.StringVar()
        grade_menu = ttk.Combobox(controls_frame, textvariable=self.filter_var, values=["All", "A+", "A", "B", "C", "D", "F"], width=5, state="readonly")
        grade_menu.current(0)
        grade_menu.grid(row=0, column=4)
        ttk.Button(controls_frame, text="Apply", command=self.apply_filter).grid(row=0, column=5, padx=5)


        text_container = ttk.Frame(main_container)
        text_container.grid(row=2, column=0, sticky="nsew")
        
        text_container.grid_rowconfigure(0, weight=1)
        text_container.grid_columnconfigure(0, weight=1) 

        scrollbar = ttk.Scrollbar(text_container)
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.text_area = tk.Text(
            text_container,
            wrap="word",
            font=("Consolas", 12),
            bg="#1E1E1E",
            fg="#FFFFFF",
            insertbackground="white",
            yscrollcommand=scrollbar.set,
            state="disabled",
            relief="flat",
            highlightthickness=0
        )
        self.text_area.grid(row=0, column=0, sticky="nsew")
        scrollbar.config(command=self.text_area.yview)

        # --- 4. Bottom Buttons ---
        btn_frame = ttk.Frame(main_container)
        btn_frame.grid(row=3, column=0, pady=(20, 0))
        ttk.Button(btn_frame, text="Load Students", command=self.load_students).pack(side="left", padx=5)
        ttk.Button(btn_frame, text="Back", command=controller.go_home).pack(side="left", padx=5)

        # Text tags
        self.text_area.tag_config("center", justify="center")
        self.text_area.tag_config("alert", foreground="#FF5555", font=("Consolas", 12, "bold"))

    def load_students(self, sort_key=None):
        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END)
        try:
            students = self.controller.manager.get_all_students()
        except AttributeError: students = []

        if sort_key:
            students.sort(key=lambda s: str(s.get(sort_key, "")).lower())

        if not students:
            self.text_area.insert(tk.END, "\nNo students found.", "center")
        else:
            for s in students:
                line = f"ID: {s['id']} | Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}\n"
                tag = "alert" if s["grade"] in ["D", "F"] else "center"
                self.text_area.insert(tk.END, line, (tag, "center"))
        self.text_area.config(state="disabled")

    def apply_filter(self):
        grade = self.filter_var.get()
        try:
            students = self.controller.manager.get_all_students()
        except AttributeError: students = []

        if grade != "All":
            students = [s for s in students if s["grade"] == grade]

        self.text_area.config(state="normal")
        self.text_area.delete(1.0, tk.END)

        if not students:
            self.text_area.insert(tk.END, "\nNo students match filter.", "center")
        else:
            for s in students:
                line = f"ID: {s['id']} | Name: {s['name']}, Age: {s['age']}, Grade: {s['grade']}\n"
                tag = "alert" if s["grade"] in ["D", "F"] else "center"
                self.text_area.insert(tk.END, line, (tag, "center"))
        self.text_area.config(state="disabled")