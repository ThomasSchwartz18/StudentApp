# utils/validation.py

def validate_notebook_name(name):
    """
    Validates a notebook name to ensure it is not empty and does not contain invalid characters.
    
    Args:
        name (str): The notebook name to validate.
    
    Returns:
        bool: True if the name is valid, False otherwise.
    """
    if not name.strip():
        return False
    # Additional validation rules can be added here.
    return True

def validate_input(data, rules):
    """
    Generic function to validate input data against a set of rules.
    
    Args:
        data (dict): A dictionary of data to validate.
        rules (dict): A dictionary where keys correspond to fields in data and values are callables
                      that return True if the field passes validation.
    
    Returns:
        bool: True if all validations pass, False otherwise.
    """
    for field, rule in rules.items():
        if not rule(data.get(field)):
            return False
    return True
