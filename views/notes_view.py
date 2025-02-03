# views/notes_view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QHBoxLayout, QLineEdit
from controllers.notes_controller import get_notebooks, add_notebook
from utils.ui_helpers import create_button, create_label
from components.note_editor import NoteEditor

class NotesView(QWidget):
    def __init__(self, main_window):
        """
        Initializes the Notes view.

        Args:
            main_window (MainWindow): The main application window.
        """
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        """
        Constructs the UI elements for the notes view.
        """
        layout = QVBoxLayout(self)
        title = create_label(self, "Notes", **{"font-size": "18px", "color": "#000"})
        layout.addWidget(title)

        # Horizontal layout for adding a new notebook.
        add_layout = QHBoxLayout()
        self.notebook_input = QLineEdit(self)
        add_layout.addWidget(self.notebook_input)
        add_button = create_button(self, "Add Notebook", self.add_notebook_action)
        add_layout.addWidget(add_button)
        layout.addLayout(add_layout)

        # List widget to display existing notebooks.
        self.notebook_list = QListWidget(self)
        layout.addWidget(self.notebook_list)
        self.load_notebooks()

        # Include the note editor component.
        self.note_editor = NoteEditor(self)
        layout.addWidget(self.note_editor)

        # Back button to return to the dashboard.
        back_button = create_button(self, "Back", self.main_window.go_back)
        layout.addWidget(back_button)
        self.setLayout(layout)

    def load_notebooks(self):
        """
        Loads and displays the list of notebooks from the model.
        """
        self.notebook_list.clear()
        notebooks = get_notebooks()
        for notebook_id, notebook in notebooks.items():
            self.notebook_list.addItem(f"{notebook_id}: {notebook['name']}")

    def add_notebook_action(self):
        """
        Reads the notebook name from the input field, adds a new notebook, and refreshes the list.
        """
        name = self.notebook_input.text().strip()
        if name:
            add_notebook(name)
            self.load_notebooks()
            self.notebook_input.clear()
