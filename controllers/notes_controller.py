# controllers/notes_controller.py
from models.notes_model import NotesModel

def get_notebooks():
    """
    Retrieves all notebooks from the model.
    
    Returns:
        dict: A dictionary of notebooks.
    """
    return NotesModel.get_notebooks()

def add_notebook(name):
    """
    Creates a new notebook with the provided name.
    
    Args:
        name (str): The notebook name.
    
    Returns:
        int: The identifier for the new notebook.
    """
    return NotesModel.add_notebook(name)

def remove_notebook(notebook_id):
    """
    Deletes a notebook from the model.
    
    Args:
        notebook_id (int): The notebook identifier.
    
    Returns:
        dict or None: The removed notebook data or None if not found.
    """
    return NotesModel.remove_notebook(notebook_id)

def add_note(notebook_id, note_data):
    """
    Adds a new note to a specified notebook.
    
    Args:
        notebook_id (int): The identifier of the notebook.
        note_data (dict): Data for the new note.
    
    Returns:
        int or None: The new note's identifier or None if the notebook was not found.
    """
    return NotesModel.add_note(notebook_id, note_data)

def remove_note(notebook_id, note_id):
    """
    Removes a note from a notebook.
    
    Args:
        notebook_id (int): The identifier of the notebook.
        note_id (int): The identifier of the note.
    
    Returns:
        dict or None: The removed note data or None if not found.
    """
    return NotesModel.remove_note(notebook_id, note_id)
