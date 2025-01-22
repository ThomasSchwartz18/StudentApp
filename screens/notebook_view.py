import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
import json
import os


class NotebookView(tk.Toplevel):
    def __init__(self, parent, json_file="notebooks.json"):
        super().__init__(parent)
        self.style = Style("flatly")  # Set the theme
        self.title("Notebook Dashboard")
        self.geometry("800x600")

        self.json_file = json_file
        self.page_file = "pages.json"  # File to save page content
        self.notebooks = self.load_notebooks()  # Load notebooks from the JSON file
        self.pages = self.load_pages()  # Load pages from the JSON file
        self.selected_notebook = None
        self.selected_page = None

        # Create the main PanedWindow
        self.main_paned_window = ttk.PanedWindow(self, orient="horizontal")
        self.main_paned_window.pack(fill="both", expand=True)

        # Left section: Notebook list
        self.left_frame = ttk.Frame(self.main_paned_window, padding=10, relief="ridge")
        self.refresh_notebook_list()  # Populate the notebook list
        self.main_paned_window.add(self.left_frame, weight=1)

        # Right section: Placeholder for dynamic content
        self.right_frame = ttk.Frame(self.main_paned_window, padding=10, relief="ridge")
        self.show_create_notebook_ui()  # Start with the Create Notebook UI
        self.main_paned_window.add(self.right_frame, weight=1)

        # Context menu for notebook actions
        self.context_menu = tk.Menu(self, tearoff=0)
        self.context_menu.add_command(label="Delete", command=self.delete_selected_notebook)

    def load_notebooks(self):
        """Load notebooks from the JSON file."""
        if os.path.exists(self.json_file):
            with open(self.json_file, "r") as file:
                return json.load(file)
        return {}

    def load_pages(self):
        """Load pages from the JSON file."""
        if os.path.exists(self.page_file):
            with open(self.page_file, "r") as file:
                return json.load(file)
        return {}

    def save_notebooks(self):
        """Save the current notebooks to the JSON file."""
        with open(self.json_file, "w") as file:
            json.dump(self.notebooks, file, indent=4)

    def save_pages(self):
        """Save the current pages to the JSON file."""
        with open(self.page_file, "w") as file:
            json.dump(self.pages, file, indent=4)

    def refresh_notebook_list(self):
        """Refresh the notebook list."""
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        left_label = ttk.Label(self.left_frame, text="Notebooks", anchor="center", font=("Helvetica", 14))
        left_label.pack(side="top", fill="x")

        notebook_container = ttk.Frame(self.left_frame)
        notebook_container.pack(side="top", fill="both", expand=True)

        for notebook in self.notebooks.keys():
            notebook_button = ttk.Button(
                notebook_container,
                text=notebook,
                command=lambda nb=notebook: self.open_notebook_pages(nb),
            )
            notebook_button.pack(side="top", fill="x", pady=5)

    def open_notebook_pages(self, notebook):
        """Split the notebook list into notebook and pages section."""
        self.selected_notebook = notebook

        # Ensure the notebook has a dictionary for pages
        if notebook not in self.pages or not isinstance(self.pages[notebook], dict):
            self.pages[notebook] = {"Page 1": ""}  # Automatically create a page if none exist
            self.save_pages()

        # Split the left frame into two sections
        for widget in self.left_frame.winfo_children():
            widget.destroy()

        notebook_list_frame = ttk.Frame(self.left_frame)
        notebook_list_frame.pack(side="left", fill="both", expand=True)

        notebook_label = ttk.Label(notebook_list_frame, text="Notebooks", font=("Helvetica", 14))
        notebook_label.pack(side="top", fill="x")

        for notebook_name in self.notebooks.keys():
            ttk.Button(
                notebook_list_frame,
                text=notebook_name,
                command=lambda nb=notebook_name: self.open_notebook_pages(nb),
            ).pack(side="top", fill="x", pady=5)

        # Pages section
        pages_frame = ttk.Frame(self.left_frame, padding=10, relief="ridge")
        pages_frame.pack(side="right", fill="both", expand=True)

        page_label = ttk.Label(pages_frame, text=f"Pages in {notebook}", font=("Helvetica", 14))
        page_label.pack(side="top", fill="x")

        for page_name in self.pages[notebook].keys():
            ttk.Button(
                pages_frame,
                text=page_name,
                command=lambda pg=page_name: self.edit_page_content(notebook, pg),
            ).pack(side="top", fill="x", pady=5)

    def edit_page_content(self, notebook, page):
        """Display and edit the content of a selected page."""
        self.selected_page = page

        # Clear the right frame
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        page_label = ttk.Label(self.right_frame, text=f"{notebook} - {page}", font=("Helvetica", 14))
        page_label.pack(side="top", pady=10)

        page_text = tk.Text(self.right_frame, wrap="word", font=("Helvetica", 12))
        page_text.pack(fill="both", expand=True)

        # Load page content if it exists
        page_content = self.pages[notebook][page]
        page_text.insert("1.0", page_content)

        def save_page_content():
            """Save the edited page content."""
            self.pages[notebook][page] = page_text.get("1.0", tk.END).strip()
            self.save_pages()

        save_button = ttk.Button(self.right_frame, text="Save", command=save_page_content)
        save_button.pack(side="bottom", pady=10)


    def delete_selected_notebook(self):
        """Delete the selected notebook."""
        if self.selected_notebook in self.notebooks:
            del self.notebooks[self.selected_notebook]
            self.save_notebooks()

            if self.selected_notebook in self.pages:
                del self.pages[self.selected_notebook]
                self.save_pages()

            self.refresh_notebook_list()
            self.show_create_notebook_ui()

    def show_create_notebook_ui(self):
        """Show the UI for creating a new notebook."""
        for widget in self.right_frame.winfo_children():
            widget.destroy()

        right_label = ttk.Label(self.right_frame, text="Create New Notebook", font=("Helvetica", 14))
        right_label.pack(side="top", pady=10)

        self.notebook_name_entry = ttk.Entry(self.right_frame, font=("Helvetica", 12))
        self.notebook_name_entry.pack(side="top", pady=10, fill="x")

        create_button = ttk.Button(
            self.right_frame,
            text="Create Notebook",
            command=self.create_new_notebook,
        )
        create_button.pack(side="top", pady=10)

    def create_new_notebook(self):
        """Create a new notebook."""
        notebook_name = self.notebook_name_entry.get().strip()
        if notebook_name and notebook_name not in self.notebooks:
            self.notebooks[notebook_name] = {"pages": []}  # Initialize with an empty list of pages
            self.pages[notebook_name] = {"Page 1": ""}  # Initialize the first page with default content
            self.save_notebooks()
            self.save_pages()
            self.refresh_notebook_list()
        elif notebook_name:
            tk.messagebox.showwarning("Duplicate", "Notebook already exists!")

