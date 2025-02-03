# utils/date_utils.py
from datetime import datetime

def format_date(date_obj, format_str="%Y-%m-%d"):
    """
    Converts a datetime object to a formatted string.
    
    Args:
        date_obj (datetime): The datetime object.
        format_str (str): The format string (default "YYYY-MM-DD").
    
    Returns:
        str: The formatted date string.
    """
    return date_obj.strftime(format_str)

def parse_date(date_str, format_str="%Y-%m-%d"):
    """
    Parses a date string into a datetime object.
    
    Args:
        date_str (str): The date string.
        format_str (str): The format string (default "YYYY-MM-DD").
    
    Returns:
        datetime: The resulting datetime object.
    """
    return datetime.strptime(date_str, format_str)
