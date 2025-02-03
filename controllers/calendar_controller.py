# controllers/calendar_controller.py
from models.calendar_model import CalendarModel

def get_calendar_events():
    """
    Retrieves the list of calendar events from the model.
    
    Returns:
        list: A list of event dictionaries.
    """
    return CalendarModel.get_events()

def add_calendar_event(event_data):
    """
    Adds a new event to the calendar model.
    
    Args:
        event_data (dict): Data describing the event (e.g., title, date).
    
    Returns:
        dict: The added event data.
    """
    return CalendarModel.add_event(event_data)
