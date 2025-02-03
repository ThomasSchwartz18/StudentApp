# components/note_editor.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from utils.file_utils import import_image
from components.shortcut_manager import register_shortcut

class NoteEditor(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the Note Editor component.
        
        Args:
            parent (QWidget, optional): The parent widget.
        """
        super().__init__(parent)
        self.bold_active = False  # Tracks whether bold formatting is active.
        self.italic_active = False  # Tracks whether italic formatting is active.
        self.init_ui()

    def init_ui(self):
        """
        Constructs the UI elements of the note editor.
        """
        layout = QVBoxLayout(self)
        # QTextEdit for rich text editing.
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        # Button to trigger image import.
        image_button = QPushButton("Insert Image", self)
        image_button.clicked.connect(self.insert_image)
        layout.addWidget(image_button)

        self.setLayout(layout)

        # Register keyboard shortcuts for toggling formatting.
        register_shortcut(self.text_edit, "Ctrl+B", self.toggle_bold)
        register_shortcut(self.text_edit, "Ctrl+I", self.toggle_italic)

    def toggle_bold(self):
        """
        Toggles bold formatting in the current text selection.
        """
        self.bold_active = not self.bold_active
        fmt = self.text_edit.currentCharFormat()
        # QFont.Weight: 75 for bold, 50 for normal.
        fmt.setFontWeight(75 if self.bold_active else 50)
        self.text_edit.setCurrentCharFormat(fmt)

    def toggle_italic(self):
        """
        Toggles italic formatting in the text.
        """
        self.italic_active = not self.italic_active
        fmt = self.text_edit.currentCharFormat()
        fmt.setFontItalic(self.italic_active)
        self.text_edit.setCurrentCharFormat(fmt)

    def insert_image(self):
        """
        Opens a file dialog for image selection and inserts the image into the text editor.
        """
        image_path = import_image()
        if image_path:
            # Insert the image into the QTextEdit using HTML.
            html_img = f'<img src="{image_path}" alt="Image">'
            self.text_edit.insertHtml(html_img)
