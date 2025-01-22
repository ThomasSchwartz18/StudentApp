import tkinter as tk
from tkinter import ttk, messagebox
import json
from screens.notebook_view import NotebookView


class NotesScreen(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Notes")
        self.geometry("600x400")
        self.notebooks = self.load_notebooks()

        # Notebook list
        self.notebook_list = tk.Listbox(self)
        self.notebook_list.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Buttons for notebook management
        btn_frame = ttk.Frame(self)
        btn_frame.pack(side="right", fill="y", padx=10, pady=10)

        create_btn = ttk.Button(btn_frame, text="Create Notebook", command=self.create_notebook)
        create_btn.pack(fill="x", pady=5)

        delete_btn = ttk.Button(btn_frame, text="Delete Notebook", command=self.delete_notebook)
        delete_btn.pack(fill="x", pady=5)

        open_btn = ttk.Button(btn_frame, text="Open Notebook", command=self.open_notebook)
        open_btn.pack(fill="x", pady=5)

        self.refresh_notebook_list()

    def load_notebooks(self):
        try:
            with open("data/notebooks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_notebooks(self):
        with open("data/notebooks.json", "w") as file:
            json.dump(self.notebooks, file)

    def refresh_notebook_list(self):
        self.notebook_list.delete(0, tk.END)
        for notebook in self.notebooks.keys():
            self.notebook_list.insert(tk.END, notebook)

    def create_notebook(self):
        name = tk.simpledialog.askstring("Create Notebook", "Enter notebook name:")
        if name and name not in self.notebooks:
            self.notebooks[name] = []
            self.save_notebooks()
            self.refresh_notebook_list()
        elif name:
            messagebox.showwarning("Duplicate", "Notebook already exists!")

    def delete_notebook(self):
        selected = self.notebook_list.curselection()
        if selected:
            notebook_name = self.notebook_list.get(selected)
            del self.notebooks[notebook_name]
            self.save_notebooks()
            self.refresh_notebook_list()

    def open_notebook(self):
        selected = self.notebook_list.curselection()
        if selected:
            notebook_name = self.notebook_list.get(selected)
            NotebookView(self, notebook_name, self.notebooks[notebook_name], self.save_notebooks)
