# controllers/dashboard_controller.py
from views.calendar_view import CalendarView
from views.notes_view import NotesView

def open_calendar(main_window):
    """
    Processes the dashboard request to open the Calendar view.
    
    Args:
        main_window (MainWindow): The main application window instance.
    """
    # Instantiate CalendarView and delegate navigation to the main window.
    calendar_view = CalendarView(main_window)
    main_window.navigate_to(calendar_view)

def open_notes(main_window):
    """
    Processes the dashboard request to open the Notes view.
    
    Args:
        main_window (MainWindow): The main application window instance.
    """
    # Instantiate NotesView and delegate navigation.
    notes_view = NotesView(main_window)
    main_window.navigate_to(notes_view)
