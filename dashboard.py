import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from screens.notebook_view import NotebookView  # Import NotebookView


class Dashboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.style = Style("flatly")  # Set the theme
        self.title("Student Dashboard")
        self.geometry("800x600")

        # Create the main PanedWindow
        main_paned_window = ttk.PanedWindow(self, orient="horizontal")
        main_paned_window.pack(fill="both", expand=True)

        # Create the left pane (spans from top to bottom)
        left_frame = ttk.Frame(main_paned_window, padding=10, relief="ridge")
        left_label = ttk.Label(left_frame, text="Left Section\n(Notes Area)", anchor="center", font=("Helvetica", 14))
        left_label.pack(expand=True, fill="both")

        # Add a button to open NotebookView
        open_notebook_btn = ttk.Button(
            left_frame,
            text="Open Notebook",
            style="primary.TButton",
            command=self.open_notebook_view
        )
        open_notebook_btn.pack(pady=10)  # Adjust padding for spacing
        main_paned_window.add(left_frame, weight=1)  # Add to the PanedWindow

        # Create a vertical PanedWindow for the right side
        right_paned_window = ttk.PanedWindow(main_paned_window, orient="vertical")
        main_paned_window.add(right_paned_window, weight=2)

        # Create the top-right pane
        top_right_frame = ttk.Frame(right_paned_window, padding=10, relief="ridge")
        top_right_label = ttk.Label(
            top_right_frame, text="Top-Right Section\n(Grades Area)", anchor="center", font=("Helvetica", 14)
        )
        top_right_label.pack(expand=True, fill="both")
        right_paned_window.add(top_right_frame, weight=1)

        # Create the bottom-right pane
        bottom_right_frame = ttk.Frame(right_paned_window, padding=10, relief="ridge")
        bottom_right_label = ttk.Label(
            bottom_right_frame, text="Bottom-Right Section\n(Calendar Area)", anchor="center", font=("Helvetica", 14)
        )
        bottom_right_label.pack(expand=True, fill="both")
        right_paned_window.add(bottom_right_frame, weight=1)

    def open_notebook_view(self):
        """Open the NotebookView window."""
        json_file = "data/notebooks.json"  # Path to the JSON file
        NotebookView(self, json_file=json_file)

