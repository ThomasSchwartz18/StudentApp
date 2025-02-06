from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate

class CalendarController(QWidget):
    def __init__(self, parent=None):
        """
        Initializes the CalendarController with a QCalendarWidget and additional UI elements.
        """
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """
        Constructs the calendar view UI with custom styling.
        """
        # Main layout for the calendar view.
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Create a QCalendarWidget.
        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)  # Show a grid on the calendar.
        self.calendar.setMinimumDate(QDate(1900, 1, 1))  # Set the minimum date.
        self.calendar.setMaximumDate(QDate(3000, 1, 1))  # Set the maximum date.

        # Apply custom styling to the calendar.
        self.customize_calendar_style()

        # Connect the calendar's selection change signal to a slot.
        self.calendar.selectionChanged.connect(self.on_date_selected)

        # Add the calendar to the layout.
        layout.addWidget(self.calendar)

        # Label to display the selected date.
        self.date_label = QLabel("Selected Date: ", self)
        self.date_label.setStyleSheet("font-size: 16px; color: #555;")
        layout.addWidget(self.date_label)

        # Set the layout for the widget.
        self.setLayout(layout)

    def customize_calendar_style(self):
        """
        Applies custom styling to the QCalendarWidget to match the light tan theme.
        """
        self.calendar.setStyleSheet("""
            /* General calendar styling */
            QCalendarWidget {
                background-color: #f5f5dc;  /* Light tan background */
                color: #555;               /* Dark gray font color */
                font-size: 16px;
                border: 1px solid #c9c3be; /* Light gray border */
            }

            /* Header (month/year) styling */
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #e0d8c0;  /* Slightly darker tan for header */
                color: #555;               /* Dark gray font color for header */
                font-size: 18px;
                padding: 5px;
            }

            /* Month/year button styling */
            QCalendarWidget QToolButton {
                background-color: #d0c8b0;  /* Light tan for buttons */
                color: #555;               /* Dark gray font color for buttons */
                font-size: 16px;
                border: 1px solid #c9c3be; /* Light gray border */
                padding: 5px;
            }

            /* Month/year button hover effect */
            QCalendarWidget QToolButton:hover {
                background-color: #c0b8a0;  /* Slightly darker tan on hover */
                color: #555;               /* Dark gray font color on hover */
            }

            /* Weekday headers (Mon, Tue, etc.) */
            QCalendarWidget QAbstractItemView:enabled {
                color: #777;               /* Medium gray for weekday headers */
                font-size: 14px;
            }

            /* Selected date styling */
            QCalendarWidget QAbstractItemView:enabled:selected {
                background-color: #c9c3be;  /* Light gray for selected date */
                color: #333;               /* Darker gray font color for selected date */
                font-weight: bold;
            }

            /* Today's date styling */
            QCalendarWidget QAbstractItemView:enabled:!selected:today {
                background-color: #b0a898;  /* Darker tan for today's date */
                color: #333;               /* Darker gray font color for today's date */
                font-weight: bold;
            }
        """)

    def on_date_selected(self):
        """
        Slot triggered when a date is selected in the calendar.
        """
        selected_date = self.calendar.selectedDate()
        self.date_label.setText(f"Selected Date: {selected_date.toString('yyyy-MM-dd')}")