# views/dashboard_view.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSplitter
from PyQt5.QtCore import Qt
from utils.ui_helpers import create_button, create_label
from views.calendar_view import CalendarView
from views.notes_view import NotesView

check_list = """**What is done:**
    * Created file structure...............................................02/02/2025
        [folder breakdown]
    * Created utils folder.................................................02/02/2025
        [commonly used functions]
    * Notes & calendar.....................................................02/02/2025 
        [opens screens for both modules]
    * backgroud transparency...............................................02/02/2025
        [background of application is transparent]
    * control menu.........................................................02/03/2025
        [menu to close and minimize application]

**To-Dos:**
    * Work on note taking..................................................
        [add toolbar, saves, image import]
    * Add calendar.........................................................  
        [add in calendar tracking and editing]

**Future Wants:**
    * Join class........................................................... 
        [using a class code join classes to receive course material]
    * Push functionality................................................... 
        [administrators can push out files or requests]
    * Course promotions.................................................... 
        [creators can add/sell educational courses]

"""


class DashboardView(QWidget):
    def __init__(self, main_window):
        """
        Initializes the Dashboard view with a draggable splitter and a styled, thin, dotted median handle,
        with no padding for the application window, and a right section that updates with the calendar or notes screens.

        Args:
            main_window (QWidget): The main application window.
        """
        super().__init__()
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        """
        Constructs the UI elements using a QSplitter to create two resizable sections.
        """
        # Create a horizontal splitter for the left (navigation) and right (content) sections.
        splitter = QSplitter(Qt.Horizontal, self)
        # Set the handle to be a thin, dotted line.
        splitter.setHandleWidth(2)
        splitter.setStyleSheet("""
            QSplitter::handle {
                border: 1px dotted #c9c3be;
                background: transparent;
            }
        """)

        # -----------------------------
        # Left Section: Navigation Buttons
        # -----------------------------
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(0)
        
        # Button to open the Calendar view.
        calendar_button = create_button(
            left_widget,
            "Calendar",
            self.show_calendar  # Calls the method to update the right section.
        )
        left_layout.addWidget(calendar_button)
        
        # Button to open the Notes view.
        notes_button = create_button(
            left_widget,
            "Notes",
            self.show_notes  # Calls the method to update the right section.
        )
        left_layout.addWidget(notes_button)
        
        left_layout.addStretch()

        # -----------------------------
        # Right Section: Content Area
        # -----------------------------
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout(self.right_widget)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        self.right_layout.setSpacing(0)
        
        # Add a placeholder so the right section isn't empty on startup.
        placeholder = create_label(self.right_widget, check_list, font_size="16px", color="#555")
        self.right_layout.addWidget(placeholder)
        self.right_layout.addStretch()

        # Add the two sections to the splitter.
        splitter.addWidget(left_widget)
        splitter.addWidget(self.right_widget)
        # Set the initial sizes for the left and right sections.
        splitter.setSizes([200, 600])

        # -----------------------------
        # Main Layout: Add the splitter with no padding.
        # -----------------------------
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def update_right_section(self, widget):
        """
        Clears the right section and adds the provided widget.

        Args:
            widget (QWidget): The widget (CalendarView or NotesView) to display in the right section.
        """
        # Remove any existing widgets from the right layout.
        while self.right_layout.count():
            child = self.right_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        # Add the new widget.
        self.right_layout.addWidget(widget)

    def show_calendar(self):
        """
        Displays the Calendar view in the right section.
        """
        calendar_view = CalendarView(self)
        self.update_right_section(calendar_view)

    def show_notes(self):
        """
        Displays the Notes view in the right section.
        """
        notes_view = NotesView(self)
        self.update_right_section(notes_view)

    def go_back(self):
        """
        Resets the right section to its default placeholder content.
        This method can be called from subviews (e.g. CalendarView or NotesView) when a "Back" action is needed.
        """
        placeholder = create_label(self.right_widget, check_list, font_size="16px", color="#555")
        self.update_right_section(placeholder)
