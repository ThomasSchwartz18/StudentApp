from PyQt5.QtWidgets import QWidget, QVBoxLayout, QCalendarWidget, QLabel
from PyQt5.QtCore import QDate
from components.task_list import TaskList


class CalendarView(QWidget):
    def __init__(self, parent=None):
        """
        Constructs the calendar view UI with task list.
        """
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        """
        Sets up the UI layout and components.
        """
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.calendar = QCalendarWidget(self)
        self.calendar.setGridVisible(True)
        self.calendar.setMinimumDate(QDate(1900, 1, 1))
        self.calendar.setMaximumDate(QDate(3000, 1, 1))
        self.customize_calendar_style()
        layout.addWidget(self.calendar)

        self.date_label = QLabel("Selected Date: ", self)
        self.date_label.setStyleSheet("font-size: 16px; color: #555;")
        layout.addWidget(self.date_label)

        # Task List Component
        self.task_list = TaskList(self)
        layout.addWidget(self.task_list)

        self.setLayout(layout)

    def customize_calendar_style(self):
        """
        Applies custom styling to the QCalendarWidget.
        """
        self.calendar.setStyleSheet("""
            QCalendarWidget {
                background-color: #f5f5dc;
                color: #555;
                font-size: 16px;
                border: 1px solid #c9c3be;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: #e0d8c0;
                color: #555;
                font-size: 18px;
                padding: 5px;
            }
            QCalendarWidget QToolButton {
                background-color: #d0c8b0;
                color: #555;
                font-size: 16px;
                border: 1px solid #c9c3be;
                padding: 5px;
            }
        """)
