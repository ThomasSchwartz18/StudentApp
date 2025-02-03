# utils/file_utils.py
from PyQt5.QtWidgets import QFileDialog

def import_image():
    """
    Opens a file dialog to allow the user to select an image file.
    
    Returns:
        str: The path to the selected image file, or None if canceled.
    """
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly
    file_path, _ = QFileDialog.getOpenFileName(
        None,
        "Select an Image",
        "",
        "Image Files (*.png *.jpg *.jpeg *.gif);;All Files (*)",
        options=options
    )
    return file_path if file_path else None

# Additional file I/O operations like read_file or save_file can be added here.
