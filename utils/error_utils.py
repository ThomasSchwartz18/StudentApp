# utils/error_utils.py
import logging
from PyQt5.QtWidgets import QMessageBox

# Configure logging to write error messages to a file.
logging.basicConfig(
    filename='app.log',
    level=logging.ERROR,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

def log_error(message):
    """
    Logs an error message using Python's logging facility.
    
    Args:
        message (str): The error message to log.
    """
    logging.error(message)

def show_error_dialog(message):
    """
    Displays a pop-up error dialog using PyQt's QMessageBox.
    
    Args:
        message (str): The error message to display.
    """
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Error")
    msg_box.setText(message)
    msg_box.exec_()

def handle_exception(exception):
    """
    Logs an exception and displays an error dialog.
    
    Args:
        exception (Exception): The exception to handle.
    """
    log_error(str(exception))
    show_error_dialog(str(exception))
