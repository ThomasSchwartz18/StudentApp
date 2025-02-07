# utils/file_utils.py
from PyQt5.QtWidgets import QFileDialog
import json
import os

# Define the storage folder and tasks file path
STORAGE_FOLDER = "storage"
TASKS_FILE = os.path.join(STORAGE_FOLDER, "tasks.json")

# Ensure the storage directory exists
os.makedirs(STORAGE_FOLDER, exist_ok=True)

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

def load_tasks(date):
    """
    Loads tasks from the tasks.json file for a given date.
    Returns an empty list if no tasks exist for that date.
    """
    if not os.path.exists(TASKS_FILE):
        return []

    with open(TASKS_FILE, "r") as file:
        data = json.load(file)

    return data.get(date, [])


def save_tasks(date, tasks):
    """
    Saves tasks to the tasks.json file in the storage folder.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            data = json.load(file)
    else:
        data = {}

    data[date] = tasks

    with open(TASKS_FILE, "w") as file:
        json.dump(data, file, indent=4)