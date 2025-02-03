# models/notes_model.py

class NotesModel:
    # In‑memory storage for notebooks; each notebook is a dictionary with a name and notes.
    _notebooks = {}
    _next_notebook_id = 1
    _next_note_id = 1

    @classmethod
    def get_notebooks(cls):
        """
        Returns all notebooks.
        
        Returns:
            dict: Dictionary where keys are notebook IDs and values are notebook data.
        """
        return cls._notebooks

    @classmethod
    def add_notebook(cls, name):
        """
        Creates a new notebook.
        
        Args:
            name (str): The notebook’s name.
        
        Returns:
            int: The ID of the new notebook.
        """
        notebook_id = cls._next_notebook_id
        cls._notebooks[notebook_id] = {"name": name, "notes": {}}
        cls._next_notebook_id += 1
        return notebook_id

    @classmethod
    def remove_notebook(cls, notebook_id):
        """
        Deletes a notebook.
        
        Args:
            notebook_id (int): The notebook’s ID.
        
        Returns:
            dict or None: The removed notebook data, or None if not found.
        """
        return cls._notebooks.pop(notebook_id, None)

    @classmethod
    def add_note(cls, notebook_id, note_data):
        """
        Adds a new note to a specified notebook.
        
        Args:
            notebook_id (int): The target notebook’s ID.
            note_data (dict): The note’s details.
        
        Returns:
            int or None: The new note’s ID or None if the notebook does not exist.
        """
        if notebook_id in cls._notebooks:
            note_id = cls._next_note_id
            cls._notebooks[notebook_id]["notes"][note_id] = note_data
            cls._next_note_id += 1
            return note_id
        return None

    @classmethod
    def remove_note(cls, notebook_id, note_id):
        """
        Removes a note from a notebook.
        
        Args:
            notebook_id (int): The notebook’s ID.
            note_id (int): The note’s ID.
        
        Returns:
            dict or None: The removed note data, or None if not found.
        """
        if notebook_id in cls._notebooks:
            return cls._notebooks[notebook_id]["notes"].pop(note_id, None)
        return None
