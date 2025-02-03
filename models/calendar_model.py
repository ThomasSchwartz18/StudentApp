# models/calendar_model.py

class CalendarModel:
    # In‑memory list to store event dictionaries.
    _events = []

    @classmethod
    def get_events(cls):
        """
        Returns the current list of calendar events.
        
        Returns:
            list: The list of events.
        """
        return cls._events

    @classmethod
    def add_event(cls, event_data):
        """
        Appends a new event to the calendar.
        
        Args:
            event_data (dict): Dictionary containing event details.
        
        Returns:
            dict: The event data that was added.
        """
        cls._events.append(event_data)
        return event_data

    @classmethod
    def remove_event(cls, event_index):
        """
        Removes an event by its index.
        
        Args:
            event_index (int): The index position of the event in the list.
        
        Returns:
            dict or None: The removed event, or None if the index is invalid.
        """
        if 0 <= event_index < len(cls._events):
            return cls._events.pop(event_index)
        return None
