# views/calendar_view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget
from controllers.calendar_controller import get_calendar_events
from utils.ui_helpers import create_button, create_label

class CalendarView(QWidget):
    def __init__(self, main_window):
        """
        Initializes the Calendar view.

        Args:
            main_window (MainWindow): The main application window.
        """
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        """
        Constructs the UI elements for the calendar view.
        """
        layout = QVBoxLayout(self)
        title = create_label(self, "Calendar", **{"font-size": "18px", "color": "#000"})
        layout.addWidget(title)

        # List widget to display calendar events.
        self.event_list = QListWidget(self)
        layout.addWidget(self.event_list)
        self.load_events()

        # Back button to return to the previous view.
        back_button = create_button(
            self,
            "Back",
            self.main_window.go_back
        )
        layout.addWidget(back_button)
        self.setLayout(layout)

    def load_events(self):
        """
        Retrieves events from the controller and populates the list widget.
        """
        events = get_calendar_events()
        self.event_list.clear()
        for event in events:
            # Assume each event is a dict with a "title" key.
            self.event_list.addItem(event.get("title", "Untitled Event"))
